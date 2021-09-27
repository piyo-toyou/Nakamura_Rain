# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Created on August 02 2021.
@author: W.KOGA
各雨量データのグラフを作成する。
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# モジュールのインポート
import pandas as pd
import numpy as np
import matplotlib as mpl
import math
import matplotlib.pylab as plt
import datetime

# パス設定
DataPATH = "G:/マイドライブ/Nakamura_Rain/"

# 図のフォントの設定
mpl.rcParams['font.family'] = 'MS Gothic'

# 図の作成
df1   = pd.read_excel(DataPATH + "Nakamura_Rain.xlsx", header=0, index_col=0)
x     = np.array(df1.columns.values)
y1   = np.array(df1.loc['窪川・時間'])
y2   = np.array(df1.loc['窪川・連続'])

# 作図範囲の設定
n = 36
if len(x) > n:
    x = np.delete(x, slice(0, -n))
    y1 = np.delete(y1, slice(0, -n))
    y2 = np.delete(y2, slice(0, -n))
else:
    pass

# 図・座標軸の設定
fig = plt.figure(figsize=(10,6))
ax1 = fig.subplots()
ax2 = ax1.twinx()
fig.subplots_adjust(bottom=0.35)

# データのプロット
ax1.bar(x, y1,
 width=0.2, color="navy", label="時間雨量（mm）")
ax2.plot(x, y2,
 linestyle = "solid", linewidth = 1.0, c="tomato", marker='o', label="連続雨量（mm）")

# x軸,y軸の範囲
ax1.set_ylim(0, max(y1)+10)
ax2.set_ylim(0, max(y2)+50)

# 軸ラベル名
ax1.set_ylabel('時間雨量（mm）', fontsize=10, labelpad=5)
ax2.set_ylabel('連続雨量（mm）', fontsize=10, labelpad=5)

# 軸メモリラベル
ax1.set_xticks(x)
ax1.set_xticklabels(x, rotation=90)

# 凡例の有無・大きさ・位置
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, fontsize=10, edgecolor="black")

plt.show() 
