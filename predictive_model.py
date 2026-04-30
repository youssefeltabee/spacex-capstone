#!/usr/bin/env python3
"""Predictive classification model for SpaceX launch success.
Uses dataset_part_2.csv and dataset_part_3.csv features to predict Class (success=1).
Outputs: model metrics, feature importances, and visualizations.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load data
    df2 = pd.read_csv('dataset_part_2.csv')
    df3 = pd.read_csv('dataset_part_3.csv')
    
    # Merge for features
    df = df2.merge(df3, on='FlightNumber', suffixes=('', '_dup'), how='left')
    # Use numeric and encoded features
    feature_cols = ['PayloadMass','Flights','GridFins','Reused','Legs','Block','ReusedCount']
    # Add orbit dummies (already in df3) and launch site dummies
    orbit_cols = [c for c in df.columns if c.startswith('Orbit_')]
    site_cols = [c for c in df.columns if c.startswith('LaunchSite_')]
    serial_cols = [c for c in df.columns if c.startswith('Serial_')]
    booster_cols = [c for c in df.columns if c.startswith('BoosterVersion_') or c == 'BoosterVersion']
    
    # Prepare X
    X = df[feature_cols].copy()
    if orbit_cols:
        X = pd.concat([X, df[orbit_cols]], axis=1)
    if site_cols:
        X = pd.concat([X, df[site_cols]], axis=1)
    # Fill NaN
    X = X.fillna(0)
    y = df['Class'].astype(str).str.strip().astype(int)
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Scale
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)
    
    # Models
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, class_weight='balanced'),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    }
    
    results = {}
    for name, model in models.items():
        model.fit(X_train_s, y_train)
        y_pred = model.predict(X_test_s)
        y_prob = model.predict_proba(X_test_s)[:,1]
        auc = roc_auc_score(y_test, y_prob)
        report = classification_report(y_test, y_pred, output_dict=True)
        results[name] = {
            'model': model,
            'auc': auc,
            'report': report,
            'y_test': y_test,
            'y_pred': y_pred,
            'y_prob': y_prob
        }
        print(f'\n{name}:')
        print(f'AUC: {auc:.3f}')
        print(classification_report(y_test, y_pred))
    
    # Feature importance for RF
    rf = results['Random Forest']['model']
    importances = rf.feature_importances_
    feat_df = pd.DataFrame({'feature': X.columns, 'importance': importances}).sort_values('importance', ascending=False)
    print('\nTop 10 features (Random Forest):')
    print(feat_df.head(10))
    
    # Save feature importance plot
    plt.figure(figsize=(10,6))
    sns.barplot(data=feat_df.head(15), x='importance', y='feature')
    plt.title('Top 15 Feature Importances (Random Forest)')
    plt.tight_layout()
    plt.savefig('feature_importance.png', dpi=150)
    plt.close()
    print('Saved feature_importance.png')
    
    # ROC curve plot
    plt.figure(figsize=(8,6))
    for name, res in results.items():
        fpr, tpr, _ = roc_curve(res['y_test'], res['y_prob'])
        plt.plot(fpr, tpr, label=f"{name} (AUC={res['auc']:.3f})")
    plt.plot([0,1],[0,1],'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves')
    plt.legend()
    plt.tight_layout()
    plt.savefig('roc_curves.png', dpi=150)
    plt.close()
    print('Saved roc_curves.png')
    
    # Confusion matrix for best model
    best = 'Random Forest'  # typically better
    cm = confusion_matrix(results[best]['y_test'], results[best]['y_pred'])
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Pred Fail','Pred Success'], yticklabels=['Act Fail','Act Success'])
    plt.title(f'Confusion Matrix - {best}')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png', dpi=150)
    plt.close()
    print('Saved confusion_matrix.png')
    
    # Save results summary
    with open('predictive_results.txt', 'w') as f:
        f.write('SpaceX Launch Success - Predictive Model Results\n')
        f.write('='*50 + '\n\n')
        for name, res in results.items():
            f.write(f'{name}:\n')
            f.write(f"  AUC: {res['auc']:.3f}\n")
            f.write(f"  Precision (class 1): {res['report']['1']['precision']:.3f}\n")
            f.write(f"  Recall (class 1): {res['report']['1']['recall']:.3f}\n")
            f.write(f"  F1-score (class 1): {res['report']['1']['f1-score']:.3f}\n\n")
        f.write('Top 10 Feature Importances (Random Forest):\n')
        for _, row in feat_df.head(10).iterrows():
            f.write(f"  {row['feature']}: {row['importance']:.4f}\n")
    print('Saved predictive_results.txt')

if __name__ == '__main__':
    main()
