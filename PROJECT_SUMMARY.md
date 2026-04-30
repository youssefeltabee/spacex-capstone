# SpaceX Capstone Project - Summary & Memory

## What Was Requested
User asked for a "datascientest expert report level" based on files in:
`C:\Users\youssef besheer\Desktop\Capstone`

Specific requirements (Coursera grading):
1. Link to GitHub repository containing all completed notebooks and Python files
2. Completed presentation submitted in PDF format
3. Executive Summary slide
4. Introduction slide
5. Data collection and data wrangling methodology slides
6. EDA and interactive visual analytics methodology slides
7. Predictive analysis methodology slides
8. EDA with visualization results slides
9. EDA with SQL results slides
10. Interactive map results using Folium
11. Plotly Dash dashboard results slides
12. Predictive analysis (classification) results slides
13. Conclusion slide
14. Creativity applied to enhance the presentation beyond the given template
15. Inclusion of innovative insights

## What Was Delivered

### Files in Repository (https://github.com/youssefeltabee/spacex-capstone)
- `SpaceX_Capstone_Complete.pdf` — 14-page PDF with all required slides ✓
- `SpaceX_Capstone_Complete.pptx` — Editable PowerPoint source
- `spacex_launch_map.html` — Interactive Folium map (green=success, red=failure)
- `spacex-dash-app.py` — Plotly Dash dashboard script
- `dataset_part_1.csv`, `dataset_part_2.csv`, `dataset_part_3.csv` — Cleaned datasets
- `Spacex.csv`, `spacex_launch_dash.csv`, `spacex_web_scraped.csv` — Raw/supplementary data
- `my_data1.db` — SQLite database
- `edadataviz.ipynb` — EDA notebook
- `jupyter-labs-*.ipynb`, `lab_jupyter_*.ipynb` — All Coursera notebooks
- `SpaceX_Machine Learning Prediction_Part_5.ipynb` — ML notebook
- `.gitignore` — Prevents temp files from being tracked

### Key Statistics Computed
- Total launches analyzed: 90
- Successes: 60 (66.67%)
- Failures: 30
- Launch site success rates:
  - KSC LC 39A: 77.27% (22 launches)
  - VAFB SLC 4E: 76.92% (13 launches)
  - CCAFS SLC 40: 60.00% (55 launches)
- Orbit success rates:
  - GTO: 51.85% (27 launches)
  - ISS: 61.90% (21 launches)
  - VLEO: 85.71% (14 launches)
- Predictive model (Random Forest): AUC = 0.926
- Top features: ReusedCount (0.24), Legs (0.18), GridFins (0.16)

### Scripts Created (then removed after use to clean folder)
- `generate_capstone_reports.py` — Generated PDF, PPTX, notebook
- `populate_pptx.py` — Populated template with all slides
- `generate_pdf_slides.py` — Generated PDF from scratch
- `predictive_model.py` — Random Forest + Logistic Regression
- `folium_map.py` — Interactive map
- `spacex_summary.py` — Summary statistics
- `spacex_queries.sql` — SQL queries for SQLite

## How to Reproduce
1. Clone repo: `git clone https://github.com/youssefeltabee/spacex-capstone.git`
2. Open `SpaceX_Capstone_Complete.pdf` for final submission
3. Open `SpaceX_Capstone_Complete.pptx` in PowerPoint to edit
4. Run `spacex-dash-app.py` for interactive dashboard
5. Open `spacex_launch_map.html` in browser for Folium map

## Grading Checklist (All ✓)
✓ 1. GitHub repository link
✓ 2. PDF presentation
✓ 3. Executive Summary slide
✓ 4. Introduction slide
✓ 5. Data collection and wrangling methodology slides
✓ 6. EDA and interactive visual analytics methodology slides
✓ 7. Predictive analysis methodology slides
✓ 8. EDA with visualization results slides
✓ 9. EDA with SQL results slides
✓ 10. Interactive map results using Folium
✓ 11. Plotly Dash dashboard results slides
✓ 12. Predictive analysis (classification) results slides
✓ 13. Conclusion slide
✓ 14. Creativity applied to enhance the presentation beyond the given template
✓ 15. Inclusion of innovative insights

## Notes
- User's Windows username: `youssef besheer` (space in path)
- PowerShell used (not bash) — `&&` not supported, use `;` or separate commands
- Python 3.11.9, seaborn, matplotlib, pandas, reportlab, python-pptx all used
- Git repo initialized locally, pushed to GitHub successfully
- Folder cleaned before final push (removed temp files, scripts, figures)

## Date
Completed: April 30, 2026
