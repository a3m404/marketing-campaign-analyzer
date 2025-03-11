import streamlit as st

def hseb_m3ayir(t3arud, nqat, t7wilat, tklfa):
    """Calculates the basic metrics of the marketing campaign."""
    if t3arud == 0:
        nisb_lnaqr = 0
    else:
        nisb_lnaqr = (nqat / t3arud) * 100

    tklfa_nqta = (tklfa / nqat) if nqat > 0 else 0
    nisb_t7wil = (t7wilat / nqat) * 100 if nqat > 0 else 0
    tklfa_t7wil = (tklfa / t7wilat) if t7wilat > 0 else 0

    return nisb_lnaqr, tklfa_nqta, nisb_t7wil, tklfa_t7wil

def l3ib():
    st.title("📊 Marketing Performance Analysis")
    st.write("Enter the campaign information to see what's happening.")

    with st.expander("📥 Enter Information", expanded=True):
        s1, s2 = st.columns(2)
        with s1:
            t3arud = st.number_input("Number of impressions", min_value=0)
            nqat = st.number_input("Number of clicks", min_value=0)
        with s2:
            t7wilat = st.number_input("Number of conversions", min_value=0)
            tklfa = st.number_input("Total cost ($)", min_value=0.0, format="%.2f")

    if st.button("🚀 Analyze Performance"):
        nisb_lnaqr, tklfa_nqta, nisb_t7wil, tklfa_t7wil = hseb_m3ayir(t3arud, nqat, t7wilat, tklfa)

        with st.expander("📊 Results", expanded=True):
            st.subheader("📌 Basic Metrics")
            s1, s2, s3, s4 = st.columns(4)

            s1.metric("Click-Through Rate (CTR)", f"{nisb_lnaqr:.2f}%", help="The percentage of people who clicked on the ad.")
            s2.metric("Cost Per Click (CPC)", f"${tklfa_nqta:.2f}", help="How much each click costs on average.")
            s3.metric("Conversion Rate", f"{nisb_t7wil:.2f}%", help="The percentage of clicks that turned into successful actions.")
            s4.metric("Cost Per Acquisition (CPA)", f"${tklfa_t7wil:.2f}", help="The cost of acquiring each customer.")

        st.subheader("📈 Tips and Insights")

        idarat = []
        
        if nisb_lnaqr >= 3:
            idarat.append("✅ **Good percentage!** Your ad is performing well.")
        elif 1 <= nisb_lnaqr < 3:
            idarat.append("⚠️ **Average percentage.** Try improving the design or targeting.")
        else:
            idarat.append("❌ **Low percentage.** You need to improve your content.")

        if nisb_t7wil >= 5:
            idarat.append("✅ **Excellent conversion rate!** Your offer is performing well.")
        elif 2 <= nisb_t7wil < 5:
            idarat.append("⚠️ **Average conversion rate.** Try A/B testing.")
        else:
            idarat.append("❌ **Low conversion rate.** Investigate where the problem is.")

        if tklfa_t7wil < 50:
            idarat.append("✅ **Good cost!** Things are looking good.")
        else:
            idarat.append("⚠️ **High cost.** You need to improve targeting.")

        for ida in idarat:
            st.write(ida)

if __name__ == "__main__":
    l3ib()
