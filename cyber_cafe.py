import streamlit as st
from google import genai

# ওয়েবসাইটের পেজ সেটআপ (ট্যাব টাইটেল এবং চওড়া স্ক্রিন)
st.set_page_config(page_title="ডিজিটাল সাইবার ক্যাফে", page_icon="💻", layout="wide")

# ওয়েবসাইটের হেডিং
st.title("💻 BISWAS DIGITAL CYBER CAFE AND CSCCENTRE")
st.write("এখানে সমস্ত রকম অনলাইন ফর্ম ফিলাপ, ই-গভর্ন্যান্স এবং ডিজিটাল পরিষেবা দেওয়া হয়।")

# সার্ভিস লিস্ট (দুটি কলামে ভাগ করে দেখানো)
st.header("আমাদের সেবাসমূহ")
col1, col2 = st.columns(2)

with col1:
    st.success("✅ প্যান কার্ড ও আধার কার্ড সংশোধন")
    st.success("✅ বাংলারভূমি (জমির রেকর্ড ও মিউটেশন)")
    st.success("✅ আয়ুষ্মান ভারত ও PM-JAY ই-কেওয়াইসি")
    st.success("✅ West Bengal e-District সার্টিফিকেটস")

with col2:
    st.success("✅ ই-রেশন কার্ড আপডেট")
    st.success("✅ CSC এবং TEC রেজিস্ট্রেশন সহায়তা")
    st.success("✅ এগ্রিস্ট্যাক (AgriStack) কৃষক আইডি")
    st.success("✅ ইনকাম ট্যাক্স (ITR) ও GST রিটার্ন ফাইলিং")

# এআই অ্যাসিস্ট্যান্ট (Gemini API ব্যবহার করে)
st.divider()
st.header("🤖 স্মার্ট এআই হেল্পডেস্ক")
st.write("যেকোনো স্কিম, ফর্ম ফিলাপের নিয়ম বা পোর্টাল সংক্রান্ত প্রশ্ন থাকলে এখানে লিখুন:")

# ইউজারের প্রশ্ন নেওয়ার জায়গা
user_query = st.text_input("আপনার প্রশ্ন লিখুন (যেমন: প্যান কার্ড সংশোধনের জন্য কী কী ডকুমেন্টস লাগে?)...")

if st.button("উত্তর খুঁজুন"):
    if user_query:
        try:
            # তোমার API Key এখানে বসাও
            client = genai.Client(api_key="AQ.Ab8RN6LT3NadsmkBPPTpH6IHdW_QBGj77oEmvhChTDUEheb2Wg") 
            
            # AI-কে নির্দেশ দেওয়া হচ্ছে সে যেন সাইবার ক্যাফের স্টাফ হিসেবে উত্তর দেয়
            prompt = f"তুমি একটি সাইবার ক্যাফের স্টাফ। কাস্টমারের এই প্রশ্নের সহজ ও সঠিক উত্তর দাও: {user_query}"
            
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )
            st.info(response.text)
        except Exception as e:
            st.error("উত্তর খুঁজতে সমস্যা হচ্ছে। দয়া করে একটু পর আবার চেষ্টা করুন।")