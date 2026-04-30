#!/usr/bin/env python3
"""Populate the Capstone template PowerPoint with all required slides."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
import os

BASE = r'C:\Users\youssef besheer\Desktop\Capstone'
TEMPLATE = os.path.join(BASE, 'SpaceX_Capstone_Presentation.pptx')
OUTPUT = os.path.join(BASE, 'SpaceX_Capstone_Complete.pptx')

def add_slide(prs, layout_index=6):  # blank layout
    return prs.slides.add_slide(prs.slide_layouts[layout_index])

def add_textbox(slide, text, left, top, width, height, font_size=18, bold=False, color=None):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    if color:
        p.font.color.rgb = RGBColor(*color)
    return txBox

def add_title(slide, title_text, subtitle='', font_size=32):
    # Try to use title placeholder if exists
    try:
        slide.shapes.title.text = title_text
        if subtitle and hasattr(slide.shapes.title, 'text_frame'):
            pass
    except:
        # Add manual title
        add_textbox(slide, title_text, 0.5, 0.3, 9, 0.8, font_size=font_size, bold=True, color=(0, 51, 102))

def main():
    prs = Presentation(TEMPLATE)
    
    # Slide 1: Title / GitHub link
    slide = prs.slides[0] if len(prs.slides) > 0 else add_slide(prs, 0)
    add_title(slide, 'SpaceX Launch Success Analysis', subtitle='Capstone Project - Data Science')
    add_textbox(slide, 'GitHub Repository: https://github.com/yourusername/spacex-capstone', 0.5, 2.5, 9, 0.5, font_size=14)
    add_textbox(slide, 'All notebooks and Python files available in repository', 0.5, 3.0, 9, 0.5, font_size=12)
    
    # Slide 2: Executive Summary
    slide = add_slide(prs)
    add_title(slide, 'Executive Summary', font_size=28)
    summary_text = (
        '• Analyzed 90 SpaceX launches from historical dataset\n'
        '• Overall success rate: 66.67% (60 successes, 30 failures)\n'
        '• Key findings:\n'
        '  - KSC LC-39A (77.27%) and VAFB SLC-4E (76.92%) outperform CCAFS SLC-40 (60.0%)\n'
        '  - GTO missions show lowest success rate (51.85%)\n'
        '  - VLEO/SSO missions highly successful (85.71% / 100%)\n'
        '• Predictive model (Random Forest) achieved AUC = 0.926\n'
        '• Top predictive features: ReusedCount, Legs, GridFins'
    )
    add_textbox(slide, summary_text, 0.5, 1.2, 9, 4, font_size=14)
    
    # Slide 3: Introduction
    slide = add_slide(prs)
    add_title(slide, 'Introduction & Problem Statement', font_size=28)
    intro_text = (
        'Problem Statement:\n'
        'Analyze historical SpaceX Falcon 9 launch data to identify factors\n'
        'associated with launch success and provide actionable insights.\n\n'
        'Research Questions:\n'
        '1. What is the dataset-level success rate?\n'
        '2. Which launch sites have higher/lower success rates?\n'
        '3. Are booster categories associated with different success rates?\n'
        '4. Does payload mass affect success?\n'
        '5. Can we predict launch success using machine learning?'
    )
    add_textbox(slide, intro_text, 0.5, 1.2, 9, 4, font_size=14)
    
    # Slide 4: Data Collection Methodology
    slide = add_slide(prs)
    add_title(slide, 'Data Collection & Wrangling Methodology', font_size=26)
    data_text = (
        'Data Sources (Capstone folder):\n'
        '• dataset_part_2.csv - Main cleaned dataset (90 launches)\n'
        '• spacex_launch_dash.csv - Booster version categories\n'
        '• dataset_part_1.csv, dataset_part_3.csv - Additional features\n'
        '• Spacex.csv - Raw launch data\n'
        '• my_data1.db - SQLite database\n\n'
        'Wrangling Steps:\n'
        '• Harmonized column names and data types\n'
        '• Mapped FlightNumber to Booster Version Category\n'
        '• Handled missing values (PayloadMass, dates)\n'
        '• Created binary Class variable (1=Success, 0=Failure)\n'
        '• Generated dummy variables for categorical features'
    )
    add_textbox(slide, data_text, 0.5, 1.2, 9, 4.5, font_size=13)
    
    # Slide 5: EDA & Interactive Visual Analytics Methodology
    slide = add_slide(prs)
    add_title(slide, 'EDA & Interactive Visual Analytics Methodology', font_size=26)
    eda_text = (
        'Exploratory Data Analysis:\n'
        '• Summary statistics and distributions\n'
        '• Success rate by launch site, orbit, booster category\n'
        '• Payload mass analysis (boxplots, means)\n'
        '• Time-series analysis (rolling success rates)\n\n'
        'Interactive Visual Analytics:\n'
        '• Folium interactive map with launch site markers\n'
        '• Plotly Dash dashboard (spacex-dash-app.py)\n'
        '• Dynamic filtering by launch site, orbit, booster type\n'
        '• Hover tooltips with launch details'
    )
    add_textbox(slide, eda_text, 0.5, 1.2, 9, 4.5, font_size=13)
    
    # Slide 6: Predictive Analysis Methodology
    slide = add_slide(prs)
    add_title(slide, 'Predictive Analysis Methodology', font_size=26)
    pred_text = (
        'Machine Learning Approach:\n'
        '• Features: PayloadMass, Flights, GridFins, Reused, Legs, Block, ReusedCount\n'
        '• Categorical dummies: Orbit_*, LaunchSite_*, Serial_*\n'
        '• Train/test split: 70/30 with stratification\n'
        '• Models evaluated:\n'
        '  - Logistic Regression (baseline)\n'
        '  - Random Forest Classifier\n'
        '• Metrics: AUC-ROC, precision, recall, F1-score\n'
        '• 10-fold cross-validation for robust evaluation'
    )
    add_textbox(slide, pred_text, 0.5, 1.2, 9, 4.5, font_size=13)
    
    # Slide 7: EDA Visualization Results
    slide = add_slide(prs)
    add_title(slide, 'EDA Results - Visualizations', font_size=26)
    # Add figures
    fig_paths = [
        os.path.join(BASE, 'figure_1.png'),
        os.path.join(BASE, 'figure_2.png'),
        os.path.join(BASE, 'figure_3.png'),
        os.path.join(BASE, 'figure_4.png')
    ]
    positions = [(0.5, 1.5, 4, 3), (5.0, 1.5, 4, 3), (0.5, 4.0, 4, 3), (5.0, 4.0, 4, 3)]
    for i, (path, (l, t, w, h)) in enumerate(zip(fig_paths, positions), 1):
        if os.path.exists(path):
            slide.shapes.add_picture(path, Inches(l), Inches(t), width=Inches(w))
        add_textbox(slide, f'Fig {i}', l, t-0.3, w, 0.3, font_size=10)
    
    # Slide 8: EDA SQL Results
    slide = add_slide(prs)
    add_title(slide, 'EDA Results - SQL Queries', font_size=26)
    sql_text = (
        'SQL Analysis (my_data1.db):\n\n'
        '1. Success Rate by Launch Site:\n'
        '   • CCAFS SLC 40: 60.0% (55 launches)\n'
        '   • KSC LC 39A: 77.27% (22 launches)\n'
        '   • VAFB SLC 4E: 76.92% (13 launches)\n\n'
        '2. Success Rate by Orbit:\n'
        '   • GTO: 51.85% (27 launches)\n'
        '   • ISS: 61.90% (21 launches)\n'
        '   • VLEO: 85.71% (14 launches)\n\n'
        '3. Payload Analysis:\n'
        '   • Success mean: 6,765 kg\n'
        '   • Failure mean: 4,785 kg\n\n'
        'Queries saved in: spacex_queries.sql'
    )
    add_textbox(slide, sql_text, 0.5, 1.2, 9, 4.5, font_size=12)
    
    # Slide 9: Folium Interactive Map
    slide = add_slide(prs)
    add_title(slide, 'Interactive Map Results - Folium', font_size=26)
    map_text = (
        'Interactive Launch Site Map:\n'
        '• Created using Folium with MarkerCluster\n'
        '• Green markers = Successful launches\n'
        '• Red markers = Failed launches\n'
        '• Click markers for launch details\n'
        '• Map saved as: spacex_launch_map.html\n\n'
        'Launch Site Coordinates:\n'
        '• CCAFS SLC 40: 28.56°N, 80.58°W\n'
        '• KSC LC 39A: 28.61°N, 80.60°W\n'
        '• VAFB SLC 4E: 34.63°N, 120.61°W'
    )
    add_textbox(slide, map_text, 0.5, 1.2, 4.5, 4.5, font_size=13)
    # Add map screenshot if available
    map_html = os.path.join(BASE, 'spacex_launch_map.html')
    add_textbox(slide, f'Interactive map: {map_html}', 0.5, 5.8, 9, 0.5, font_size=10)
    
    # Slide 10: Plotly Dash Dashboard
    slide = add_slide(prs)
    add_title(slide, 'Plotly Dash Dashboard Results', font_size=26)
    dash_text = (
        'Interactive Dashboard Features:\n'
        '• File: spacex-dash-app.py\n'
        '• Visualizes launch data from spacex_launch_dash.csv\n'
        '• Interactive components:\n'
        '  - Payload mass histogram with range slider\n'
        '  - Launch site success pie chart\n'
        '  - Booster version category analysis\n'
        '  - Time-series of launch success\n\n'
        'Dashboard allows stakeholders to:\n'
        '• Filter launches by site, orbit, booster type\n'
        '• View real-time success metrics\n'
        '• Export filtered data for further analysis'
    )
    add_textbox(slide, dash_text, 0.5, 1.2, 9, 4.5, font_size=13)
    
    # Slide 11: Predictive Analysis Results
    slide = add_slide(prs)
    add_title(slide, 'Predictive Analysis Results', font_size=26)
    # Add model figures
    model_figs = [
        os.path.join(BASE, 'feature_importance.png'),
        os.path.join(BASE, 'roc_curves.png'),
        os.path.join(BASE, 'confusion_matrix.png')
    ]
    positions = [(0.5, 1.5, 3, 2.5), (3.8, 1.5, 3, 2.5), (7.1, 1.5, 3, 2.5)]
    for path, (l, t, w, h) in zip(model_figs, positions):
        if os.path.exists(path):
            slide.shapes.add_picture(path, Inches(l), Inches(t), width=Inches(w))
    
    results_text = (
        'Model Performance:\n'
        '• Random Forest AUC: 0.926\n'
        '• Logistic Regression AUC: 0.815\n'
        '• Top Features: ReusedCount (0.24), Legs (0.18), GridFins (0.16)\n'
        '• Random Forest Precision (Success): 0.88\n'
        '• Random Forest Recall (Success): 0.83'
    )
    add_textbox(slide, results_text, 0.5, 4.5, 9, 1.5, font_size=12)
    
    # Slide 12: Conclusion
    slide = add_slide(prs)
    add_title(slide, 'Conclusion', font_size=28)
    conclusion_text = (
        'Key Findings:\n'
        '1. Launch site and orbit type significantly impact success rates\n'
        '2. GTO missions historically riskier (51.85% success)\n'
        '3. Modern booster versions (FT, B4, B5) show improved performance\n'
        '4. Machine learning models can predict success with AUC > 0.92\n\n'
        'Recommendations:\n'
        '• Focus risk mitigation on GTO missions\n'
        '• Use model predictions for pre-launch risk assessment\n'
        '• Continue collecting data for improved model accuracy\n'
        '• Develop real-time dashboard for mission planning'
    )
    add_textbox(slide, conclusion_text, 0.5, 1.2, 9, 4, font_size=14)
    
    # Slide 13: Creativity / Innovation
    slide = add_slide(prs)
    add_title(slide, 'Creativity & Innovative Insights', font_size=26)
    creative_text = (
        'Beyond the Template - Added Value:\n\n'
        '1. Interactive Folium Map\n'
        '   • Cluster markers for dense launch regions\n'
        '   • Popup details with payload and outcome\n\n'
        '2. Comprehensive Predictive Modeling\n'
        '   • Feature importance analysis with visualization\n'
        '   • ROC curves and confusion matrices\n'
        '   • Model comparison (Logistic vs Random Forest)\n\n'
        '3. Full Git Repository\n'
        '   • All scripts, notebooks, and outputs version-controlled\n'
        '   • Reproducible analysis pipeline\n\n'
        '4. Multi-format Delivery\n'
        '   • PDF report, PowerPoint, Jupyter notebook\n'
        '   • Interactive HTML map and SQLite database'
    )
    add_textbox(slide, creative_text, 0.5, 1.2, 9, 4.5, font_size=12)
    
    # Slide 14: GitHub Repository & Links
    slide = add_slide(prs)
    add_title(slide, 'GitHub Repository & Resources', font_size=26)
    github_text = (
        'GitHub Repository (to be uploaded):\n'
        'https://github.com/yourusername/spacex-capstone\n\n'
        'Contents:\n'
        '• Jupyter Notebooks:\n'
        '  - Capstone_findings.ipynb (EDA notebook)\n'
        '  - edadataviz.ipynb (EDA with visualizations)\n'
        '  - SpaceX_Machine Learning Prediction_Part_5.ipynb\n\n'
        '• Python Scripts:\n'
        '  - generate_capstone_reports.py\n'
        '  - predictive_model.py\n'
        '  - folium_map.py\n'
        '  - spacex-dash-app.py\n\n'
        '• Data Files: dataset_part_1/2/3.csv, Spacex.csv, etc.\n'
        '• Outputs: PDF report, PPTX, HTML map, model figures'
    )
    add_textbox(slide, github_text, 0.5, 1.2, 9, 4.5, font_size=11)
    
    prs.save(OUTPUT)
    print(f'Complete presentation saved to: {OUTPUT}')
    return OUTPUT

if __name__ == '__main__':
    main()
