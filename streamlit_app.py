import streamlit as st

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="Dudu Smart v25",
    page_icon="💜",
    layout="centered"
)

# واجهة تطبيق دودو سمارت
st.title("💜 Dudu Smart v25")
st.subheader("منصة الطالب الذكية والمساعدة الأكاديمية")

st.markdown("""
مرحباً بك يا مبدع في النسخة الرسمية **v25**! 
هذا التطبيق مخصص لمساعدتك في الدراسة، تلخيص المقررات، وتنظيم المهام بذكاء وسرعة فائقة.
""")

# قسم تفاعلي بسيط
user_query = st.text_input("ما الذي ترغب في بحثه أو تلخيصه اليوم؟")
if user_query:
    st.success(f"جاري معالجة طلبك حول: ({user_query}) عبر محرك دودو الذكي...")
    st.info("نعمل على تجهيز أفضل ملخص ومحتوى أكاديمي لخدمتك بدقة عالية.")

st.sidebar.title("إعدادات التطبيق")
st.sidebar.info("الإصدار: Dudu Smart v25\nتم النشر بواسطة: فوشي 🚀")import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
