# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Pagura-invoice.py.py
# Time       ：2022/3/27 15:06
# Author     ：Pagura
# Description：To print invoice
"""
book_p=52.99
lab_p=25.00
tuition_p=157.93
up_hr='*'*50
m_hr='-'*50
header="\t\tColumbus State Communtity College\n\t\t550 East Spring Street\n\t\tColumbus, OH  43215"
main="\t\tProduct Name:\tProduct Price\n\t\tBooks\t\t\t${}\n\t\tLab Fees\t\t${}\n\t\tTuition\t\t\t${}".format(book_p,lab_p,tuition_p*3)
total="\t\t\t\t\t\tTotal\n\t\t\t\t\t\t$ {}".format(book_p+lab_p+tuition_p*3)
footer="\tThank you for being a Columbus State Student"
print(up_hr)
print(header)
print(m_hr)
print(main)
print(total)
print(m_hr)
print('')
print(footer)

