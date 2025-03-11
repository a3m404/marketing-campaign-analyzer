import streamlit as st

def hseb_m3ayir(t3arud, nqat, t7wilat, tklfa):
    """كيحسب المعايير الأساسية ديال الحملة التسويقية."""
    if t3arud == 0:
        nisb_lnaqr = 0
    else:
        nisb_lnaqr = (nqat / t3arud) * 100

    tklfa_nqta = (tklfa / nqat) if nqat > 0 else 0
    nisb_t7wil = (t7wilat / nqat) * 100 if nqat > 0 else 0
    tklfa_t7wil = (tklfa / t7wilat) if t7wilat > 0 else 0

    return nisb_lnaqr, tklfa_nqta, nisb_t7wil, tklfa_t7wil

def l3ib():
    st.title("📊 تحليلة الأداء التسويقي")
    st.markdown("<div style='text-align: right;'>دخل معلومات الحملة باش نشوفو شنو واقع.</div>", unsafe_allow_html=True)

    with st.expander("📥 دخل المعلومات", expanded=True):
        s1, s2 = st.columns(2)
        with s1:
            t3arud = st.number_input("عدد العروض", min_value=0)
            nqat = st.number_input("عدد النقرات", min_value=0)
        with s2:
            t7wilat = st.number_input("عدد التحويلات", min_value=0)
            tklfa = st.number_input("التكلفة الإجمالية ($)", min_value=0.0, format="%.2f")

    if st.button("🚀 حلل الأداء"):
        nisb_lnaqr, tklfa_nqta, nisb_t7wil, tklfa_t7wil = hseb_m3ayir(t3arud, nqat, t7wilat, tklfa)

        with st.expander("📊 النتائج", expanded=True):
            st.subheader("📌 المعايير الأساسية")
            s1, s2, s3, s4 = st.columns(4)

            s1.metric("نسبة النقرات (CTR)", f"{nisb_lnaqr:.2f}%", help="النسبة المئوية ديال الناس لي ضغطو على الإعلان.")
            s2.metric("تكلفة النقرة (CPC)", f"${tklfa_nqta:.2f}", help="شحال كتكلف كل نقرة فالمتوسط.")
            s3.metric("نسبة التحويل", f"{nisb_t7wil:.2f}%", help="النسبة المئوية ديال النقرات لي تحولات لعمليات ناجحة.")
            s4.metric("تكلفة التحويل (CPA)", f"${tklfa_t7wil:.2f}", help="التكلفة ديال كل زبون مكتسب.")

        st.subheader("📈 نصائح وتحليلات")
        st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)

        idarat = []
        
        if nisb_lnaqr >= 3:
            idarat.append("✅ **النسبة زوينة!** الإعلان ديالك خدام مزيان.")
        elif 1 <= nisb_lnaqr < 3:
            idarat.append("⚠️ **النسبة وسطية.** حاول تحسن التصميم أو الاستهداف.")
        else:
            idarat.append("❌ **النسبة ضعيفة.** خاصك تزيد تحسن المحتوى ديالك.")

        if nisb_t7wil >= 5:
            idarat.append("✅ **معدل تحويل ممتاز!** العرض ديالك خدام مزيان.")
        elif 2 <= nisb_t7wil < 5:
            idarat.append("⚠️ **معدل تحويل متوسط.** جرب A/B testing.")
        else:
            idarat.append("❌ **معدل ضعيف.** شوف فين كاين المشكل.")

        if tklfa_t7wil < 50:
            idarat.append("✅ **تكلفة زوينة!** الأمور مزيانة.")
        else:
            idarat.append("⚠️ **تكلفة عالية.** خاصك تحسين الاستهداف.")

        for ida in idarat:
            st.write(ida)
        
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    l3ib()
