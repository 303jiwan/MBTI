import streamlit as st
import pandas as pd

# 📈 가상의 MBTI별 국어 성취도 데이터 생성
# 실제 데이터는 설문조사 등을 통해 수집되어야 합니다.
data = {
    'MBTI 유형': ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
                  'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'],
    '국어 성취도 (점수)': [85, 90, 92, 88, 80, 83, 95, 87,
                      78, 82, 93, 89, 86, 91, 94, 90]
}
df = pd.DataFrame(data)

# 📊 Streamlit 앱 시작
st.title('MBTI 유형별 국어 과목 성취도 분석 🧠')
st.write('자신의 MBTI 유형을 선택하여 국어 과목 성취도를 확인해보세요!')

# 🔽 MBTI 유형 선택 (스크롤)
selected_mbti = st.selectbox('MBTI 유형을 선택해주세요:', df['MBTI 유형'])

# 🔎 선택된 MBTI 유형의 성취도 결과 표시
if selected_mbti:
    result_df = df[df['MBTI 유형'] == selected_mbti]
    st.subheader(f'선택하신 **{selected_mbti}** 유형의 국어 성취도 결과입니다. ✨')
    st.table(result_df) # 표로 결과 표시

    st.write(f"평균 국어 성취도: **{df['국어 성취도 (점수)'].mean():.2f}점**")
    st.write("---")
    st.write("본 데이터는 예시이며, 실제 MBTI 유형과 국어 성취도 간의 통계적 유의미한 상관관계를 나타내지 않습니다.")
