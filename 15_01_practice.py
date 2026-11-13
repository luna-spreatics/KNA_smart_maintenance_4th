import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
log_raw = pd.read_csv(F_LOG)

print(log_raw.shape)      # (16, 7)
print(log_raw.isna().sum())
# 측정시각     0
# 사출기      1
# 배럴온도     2
# 사출압력     1
# 스크루속도    1
# 누적샷      0
# 불량여부     0
print(int(log_raw["사출압력"].eq(0).sum()))     # 2
print(int(log_raw["스크루속도"].eq(-999).sum()))     # 2
print(int(log_raw["배럴온도"].eq(999).sum()))     # 1