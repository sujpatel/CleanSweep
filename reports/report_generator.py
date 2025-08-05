import matplotlib.pyplot as plt 

def generate_report(before, after):
    labels = ['CPU', 'RAM', 'Disk']
    before_vals = [100, 100, 100]
    
    after_vals = [
        (after['cpu_percent'] / before['cpu_percent']) * 100 if before['cpu_percent'] else 0,
        (after['memory'] / before['memory']) * 100 if before['memory'] else 0,
        (after['disk'] / before ['disk']) * 100 if before['disk'] else 0
    ]
    
    x = range(len(labels))
    bar_width = 0.35
    
    plt.bar([i - bar_width/2 for i in x], before_vals, width=bar_width, label='Before')
    plt.bar([i + bar_width/2 for i in x], after_vals, width=bar_width, label='After')
    
    plt.xticks(list(x), labels)
    plt.ylabel("Relative Usage (%)")
    plt.title("System Performance Change (Normalized)")
    plt.legend()
    plt.ylim(0, 120)
    plt.tight_layout()
    plt.show()
    
    #plt.bar(x_positions, bar_heights, **options)
    
    