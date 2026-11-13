import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# 실습 1
# print(qc["검사결과"].value_counts())
# print(qc.groupby("검사결과")["온도"].agg(["mean", "std", "max"]).round(2))

# table = qc.groupby("검사결과").agg(
#   평균온도=("온도", "mean"),
#   평균냉각효율=("냉각효율", "mean"),
#   측정수=("온도", "count"),
# )
# print(table.round(2))


# # 실습 2
# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# cols = ["냉각기상태", "온도", "그룹평균", "편차"]
# print(marked[cols].head(3).round(2))
# marked["거리"] = marked["편차"].abs()
# furthest = marked.sort_values("거리", ascending=False).head(1)
# print(furthest[cols].round(2))
# #   냉각기상태    온도   그룹평균     편차
# # 0    고장  35.6  54.67 -19.07

# print(marked.groupby("냉각기상태")["편차"].sum().round(10))

# pivot = pd.pivot_table(marked, index="밸브상태", columns="운전부하", values="온도",
#                        aggfunc="mean", margins="True", margins_name="전체")
# print(pivot.round(2))
# print(pivot.shape)

# 실습 3
four_col = df[["온도", "진동", "압력", "냉각효율"]]
corr4 = four_col.corr()
print(corr4.round(3))

#       온도     진동     압력   냉각효율
# 온도    1.000  0.931  0.284 -0.951
# 진동    0.931  1.000  0.524 -0.862
# 압력    0.284  0.524  1.000 -0.131
# 냉각효율 -0.951 -0.862 -0.131  1.000

# 표를 읽어 찾은 짝을 원래 값으로 확인
print("가장 강한 짝:", round(corr4.loc["온도", "냉각효율"], 3))
print("가장 약한 짝:", round(corr4.loc["압력", "냉각효율"], 3))