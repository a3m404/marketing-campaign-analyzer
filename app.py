import streamlit as st

def calculate_kpis(impressions, clicks, conversions, cost):
    """Calculates key marketing performance indicators (KPIs)."""
    if impressions == 0:
        ctr = 0
    else:
        ctr = (clicks / impressions) * 100

    cpc = (cost / clicks) if clicks > 0 else 0
    conversion_rate = (conversions / clicks) * 100 if clicks > 0 else 0
    cpa = (cost / conversions) if conversions > 0 else 0

    return ctr, cpc, conversion_rate, cpa

def main():
    st.title("📊 Marketing Performance Analyzer")
    st.write("Enter your campaign details below to analyze key performance metrics.")

    # User Inputs  
    with st.expander("📥 Enter Campaign Data", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            impressions = st.number_input("Total Impressions", min_value=0)
            clicks = st.number_input("Total Clicks", min_value=0)
        with col2:
            conversions = st.number_input("Total Conversions", min_value=0)
            cost = st.number_input("Total Cost ($)", min_value=0.0, format="%.2f")

    if st.button("🚀 Analyze Performance"):
        ctr, cpc, conversion_rate, cpa = calculate_kpis(impressions, clicks, conversions, cost)

        with st.expander("📊 Campaign Results", expanded=True):
            st.subheader("📌 Key Metrics")
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Click-Through Rate (CTR)", f"{ctr:.2f}%", help="The percentage of users who clicked on the ad.")
            col2.metric("Cost Per Click (CPC)", f"${cpc:.2f}", help="How much each click costs on average.")
            col3.metric("Conversion Rate", f"{conversion_rate:.2f}%", help="The percentage of clicks that led to a conversion.")
            col4.metric("Cost Per Acquisition (CPA)", f"${cpa:.2f}", help="The cost to acquire a new customer.")

        # Performance Interpretation  
        st.subheader("📈 Insights & Recommendations")

        insights = []
        
        if ctr >= 3:
            insights.append("✅ **Great CTR!** Your ad is engaging well with your audience.")
        elif 1 <= ctr < 3:
            insights.append("⚠️ **Decent CTR.** Consider improving your ad creatives or targeting.")
        else:
            insights.append("❌ **Low CTR.** Try optimizing your ad visuals and messaging.")

        if conversion_rate >= 5:
            insights.append("✅ **Excellent Conversion Rate!** Your landing page and offer are performing well.")
        elif 2 <= conversion_rate < 5:
            insights.append("⚠️ **Average Conversion Rate.** You might want to A/B test different landing pages.")
        else:
            insights.append("❌ **Low Conversion Rate.** Check for friction in your conversion process.")

        if cpa < 50:
            insights.append("✅ **Good CPA!** Your cost per conversion is within a profitable range.")
        else:
            insights.append("⚠️ **High CPA.** Consider optimizing your ads or refining your target audience.")

        for insight in insights:
            st.write(insight)

if __name__ == "__main__":
    main()