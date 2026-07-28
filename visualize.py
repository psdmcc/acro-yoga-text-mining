import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File definitions matching your absolute workspace paths
CSV_PATH = "/Users/croma/acro-yoga-text-mining/outputs/metrics/gretil_somatic_density.csv"
IMG_PATH = "/Users/croma/acro-yoga-text-mining/outputs/visualizations/somatic_overlap_matrix.png"

def generate_academic_plot():
    if not os.path.exists(CSV_PATH):
        print(f"[!] Target metrics spreadsheet missing at: {CSV_PATH}")
        return

    print("[*] Parsing textual analytics table to isolate density intersections...")
    df = pd.read_csv(CSV_PATH)

    # Filter out baseline noise: isolate texts with active overlap
    overlap_df = df[(df['subaltern_tribal_raw_count'] > 0) & (df['postural_contortion_raw_count'] > 0)]

    if overlap_df.empty:
        print("[!] No overlapping hits identified yet across current regex constraints.")
        return

    # Set up clean, academic formatting styles
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)

    # Plot the texts as data points
    sns.scatterplot(
        data=overlap_df,
        x='subaltern_tribal_density_10k',
        y='postural_contortion_density_10k',
        size='total_words',
        sizes=(40, 400),
        alpha=0.6,
        color='#4A154B', # Deep academic plum accent
        edgecolor='black',
        linewidth=0.5,
        ax=ax
    )

    # Dynamic labelling: identify the top 5 outlier "smoking guns" text titles
    top_outliers = overlap_df.assign(
        combined_score=overlap_df['subaltern_tribal_density_10k'] * overlap_df['postural_contortion_density_10k']
    ).nlargest(5, 'combined_score')

    for idx, row in top_outliers.iterrows():
        # Clean up file names for visual presentation (e.g., truncate long handles)
        clean_label = row['file_name'].replace('_u.htm', '').replace('.txt', '')
        ax.annotate(
            clean_label,
            (row['subaltern_tribal_density_10k'], row['postural_contortion_density_10k']),
            textcoords="offset points",
            xytext=(5, 5),
            ha='left',
            fontsize=8,
            fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.3, ec="gray", lw=0.5)
        )

    # Layout designations
    ax.set_title("The Acro-Yoga Complex: Subaltern-Postural Semantic Overlap Matrix\n(Normalized Density Per 10k Tokens Across GRETIL)", fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel("Subaltern / Tribal Identity Vocabulary Density (Per 10k Words)", fontsize=10)
    ax.set_ylabel("Postural / Contortionist Somatic Density (Per 10k Words)", fontsize=10)
    
    # Legend formatting
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[-3:], labels[-3:], title="Manuscript Word Count", loc="upper right", frameon=True)

    plt.tight_layout()
    os.makedirs(os.path.dirname(IMG_PATH), exist_ok=True)
    plt.savefig(IMG_PATH, bbox_inches='tight')
    plt.close()
    print(f"[+] Academic plot compiled and exported cleanly to: {IMG_PATH}")

if __name__ == "__main__":
    generate_academic_plot()
