# Entropy -- Source Coding

## 1. Introduction

**source coding**-- recoverable, as short as possible (expectation) mapping from source message to a mediate coding.

​	Hoffman树-- 高频率短编码

​	大量传输的意义下，传输并不是一次完成，而是连续的传输若干个。
$$
A\rightarrow0, B\rightarrow1,C\rightarrow10,\ 引起歧义\\
A\rightarrow0, B\rightarrow11,C\rightarrow10,\ 无歧义
$$
​	码字一定存在字长下界，否则会引起歧义。

## 2. Prefix-free codes

