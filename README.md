# ML on the A14 Conington Coin Assemblage

Exploratory machine learning project using the A14 Cambridge to Huntingdon (Conington Landscape Block) coin data to practise clustering and classification on small archaeological datasets.

## Project goals

- Follow Google's ML project phases (ideation & planning, experimentation, pipeline building, productionization) on a real archaeological case study.[web:16][web:20]  
- Explore whether basic attributes (material, denomination, mint, diameter, mid/late date) show structure that aligns with numismatic regimes and periods.[file:5][file:6]  
- Build simple, interpretable ML pipelines (K-Means clustering and decision tree classification) and critically assess their usefulness given the very small, biased assemblage (~59 coins).[file:5][file:3]

## Data

- Excavation coin register: `A14_Conington_coin_data02.csv` (one row per coin with basic context, regime, dates, etc.).[file:5]  
- Numismatic/archival detail: `A14_Conington_coin_data01.xlsx` (ruler, Reece period, denomination, detailed descriptions).[^1]

> Note: These datasets originate from the A14 Cambridge to Huntingdon archaeological project and are used here for non-commercial, educational purposes.

## Methods (planned)

- Data cleaning and feature engineering (e.g. mid-date and date-span from early/late dates).  
- Exploratory data analysis and sanity checks against the published Conington reports.  
- Unsupervised learning: K-Means on selected numeric features with archaeological interpretation of clusters.  
- Supervised learning: simple decision tree classifier with cross-validation to predict `COIN_REGIME`.


[^1]: See accompanying reports for archaeological and numismatic context (Conington Landscape Block report; Conington coins specialist report).
