import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Generate synthetic data for three groups
np.random.seed(0)
group1 = np.random.normal(100, 15, 30)  # Group 1
group2 = np.random.normal(110, 20, 30)  # Group 2
group3 = np.random.normal(105, 18, 30)  # Group 3

# Shapiro-Wilk Test for normality
sw_group1 = stats.shapiro(group1)
sw_group2 = stats.shapiro(group2)
sw_group3 = stats.shapiro(group3)

# Levene's Test for homogeneity of variances
levene_test = stats.levene(group1, group2, group3)

# One-way ANOVA or Kruskal-Wallis Test (depending on normality and homogeneity)
if all([sw_group1.pvalue > 0.05, sw_group2.pvalue > 0.05, sw_group3.pvalue > 0.05]) and levene_test.pvalue > 0.05:
    # Data is normally distributed and variances are equal, perform ANOVA
    anova_test = stats.f_oneway(group1, group2, group3)
    test_used = "ANOVA"
    p_value = anova_test.pvalue
else:
    # Use Kruskal-Wallis Test
    kruskal_test = stats.kruskal(group1, group2, group3)
    test_used = "Kruskal-Wallis"
    p_value = kruskal_test.pvalue

# Prepare data for visualization
data = np.concatenate([group1, group2, group3])
labels = ['Group 1'] * len(group1) + ['Group 2'] * len(group2) + ['Group 3'] * len(group3)
df = pd.DataFrame({'Value': data, 'Group': labels})

# Plotting
plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='Value', data=df)
plt.title(f'{test_used} Test (p-value: {p_value:.5f})')
plt.show()
