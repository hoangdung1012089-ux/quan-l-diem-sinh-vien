import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu mẫu 10 sinh viên
data = {
    'Ho_va_ten': ['An', 'Binh', 'Chi', 'Dung', 'Ha', 'Lan', 'Minh', 'Nam', 'Phuc', 'Trang'],
    'Chuyen_can': [8.0, 9.0, 7.0, 8.5, 7.5, 6.0, 8.0, 7.0, 7.5, 9.0],
    'Giua_ky': [7.5, 8.0, 6.5, 9.0, 7.0, 6.0, 8.5, 7.0, 7.5, 9.0],
    'Cuoi_ky': [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 9.0, 7.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết (20% Chuyên cần + 30% Giữa kỳ + 50% Cuối kỳ)
df['Tong_ket'] = (0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']).round(2)

# Hàm xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5: return 'Giỏi'
    elif diem >= 7.0: return 'Khá'
    elif diem >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# --- Giao diện Streamlit Web App ---

# 1. Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# 2. Bảng điểm
st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

# 3. Thống kê
st.subheader("Thống kê chung")
dtb_lop = df['Tong_ket'].mean()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]
so_sv_dat = (df['Tong_ket'] >= 5).sum()

st.write(f"- Điểm trung bình của lớp: {dtb_lop:.2f}")
st.write(f"- Sinh viên cao điểm nhất: {sv_max['Ho_va_ten']} ({sv_max['Tong_ket']} điểm)")
st.write(f"- Sinh viên thấp điểm nhất: {sv_min['Ho_va_ten']} ({sv_min['Tong_ket']} điểm)")
st.write(f"- Số sinh viên đạt: {so_sv_dat}")

# 4. Tra cứu sinh viên theo Selectbox
st.subheader("Tra cứu thông tin theo sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_va_ten'])
student_info = df[df['Ho_va_ten'] == selected_student].iloc[0]

st.write(f"Chi tiết điểm của {selected_student}:")
st.write(f"- Chuyên cần: {student_info['Chuyen_can']}")
st.write(f"- Giữa kỳ: {student_info['Giua_ky']}")
st.write(f"- Cuối kỳ: {student_info['Cuoi_ky']}")
st.write(f"- Tổng kết: {student_info['Tong_ket']}")
st.write(f"- Xếp loại: {student_info['Xep_loai']}")

# 5. Biểu đồ điểm tổng kết
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(df['Ho_va_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Họ tên')
ax.set_ylabel('Điểm tổng kết')
ax.set_ylim(0, 10)
st.pyplot(fig)

# 6. Thông tin người tạo (Chữ nhỏ ở cuối trang)
st.markdown("---")
st.markdown("<p style='font-size: 12px; color: gray;'>Người tạo: Hoàng Chí Dũng - MSSV: 001208003167</p>", unsafe_allow_html=True)
