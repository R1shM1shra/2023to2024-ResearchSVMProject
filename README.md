# 2023to2024-ResearchSVMProject

**Why this Research?**

This research was created by me, Rish Mishra, in my junior year of high school as part of the AOS (Academies of Science program) in ACL (Academies of Loudoun). The program encourages students to come up with novel, induvidual research to contribute to science, and then present it at an ACL hosted event known as Science Symposium. I began ideating in 10th grade as part of the program. As of 5/12/24, I plan on extending this project to fit multiple algorithms in my senior year, and compare those errors to each other, now that I have achieved my goal of error for this particular algorithim. 

**Background Paper on Research** → 
https://docs.google.com/document/d/1fVBYfrGii1bq3rJRCgMft91kkJa1_uxy2CK3FJsnbsA/edit?usp=sharing

**Experimental Design** → 
https://docs.google.com/document/d/1fLyVFwLq529qn6ochCbikrXrt125Rvwtyapj5y0fUeE/edit?usp=sharing

**Data Used** → 
https://drive.google.com/drive/folders/1JvBAXH74DUDzjPJVConBlXtT6Yxb9rqy?usp=sharing

**Poster for Symposium** → 
https://docs.google.com/presentation/d/14j6jFhoFxv7eE9BF7bI_RxX_lACQStBQ/edit?usp=sharing&ouid=109541641759675777203&rtpof=true&sd=true


**Abstract:**

Exoplanets, or planets outside of our own solar system, give us a large addition in understanding the universe. The Kepler Space Telescope, a telescope sent to capture transits, or drops in light curves when a planet passes a star (indicating that a planet is indeed present), was launched in hopes of expanding exoplanet research. It was successful, and created the Kepler Unconfirmed and Confirmed Dataset, listing potential candidates for exoplanets, and confirmed exoplanets. In recent years, the addition of Machine Learning to aid scientists in filtering through potential exoplanets has become prevalent. In this study, a particular type of algorithm, a Non-Linear SVM, was utilized. This algorithm would classify the potential exoplanets based on known exoplanet data on a 3d coordinate system. To begin making the algorithm, preprocessing on the data with a correlation heatmap via Python 3 was utilized to identify the variables that best correlate in known exoplanets, and use that information to classify candidates. It was found that planet temperature paired with stellar radius and stellar mass coordinated with planet temperature, among other connections. Then, a SVM kernel SVC (support vector classification) algorithm was used to classify the known exoplanet data from the dataset to train the model. After training, the model was run back onto the original dataset, and presented an error of 89%, surpassing the goal of 85% set by previous papers.
