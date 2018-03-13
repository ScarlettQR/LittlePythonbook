# author='lwz'
# coding:utf-8
# !/usr/bin/env python3
import xlrd  # 加载Excel读取模块
import xlwt  # 加载Excel写入模块


def read_excel(dir_name="C:\\Cache\\", file_name='', sheet_name='', head_row=0):
    #    打开文件 读取模式
    # dir_name 是生成文件的路径
    # file_name 是需要读取的excel的名称
    # Sheetname 是需要读取的Sheet的名称
    # head_row  标题行
    workbook = xlrd.open_workbook(file_name)
    #   打开指定sheet
    sheet2 = workbook.sheet_by_name(sheet_name)

    name_list = list()    # 表名列表
    workbook_dict = {}   # 文件名字典{文件名：workbook对象}
    pre_name = ""        # 前一个表名
    row_flag = 0         # 写入文件行指针
    column_id = 1
    for i in range(head_row+1, sheet2.nrows):
        if pre_name != sheet2.cell(i, column_id).value and sheet2.cell(i, column_id).value not in name_list:
            # 判断与前一个表名是否一致 表名是否重复
            name_list.append(sheet2.cell(i, column_id).value)
            pre_name = sheet2.cell(i, column_id).value   # 获取当前表名
            fname = dir_name + pre_name + ".xlsx"  # 生成文件名
            print(fname)
            new_workbook = xlwt.Workbook(fname)  # 创建excel 得到workbook对象
            workbook_dict[fname] = new_workbook  # 记录workbook对象
            new_workbook.add_sheet("sheet1")     # 创建 sheet
            new_sheet = new_workbook.get_sheet(0)  # 获取第一个sheet

            # new_sheet.write(0, 0, sheet2.cell(1, 0).value)  # 写入表格名称  对sheet(0, 0)写入sheet2.cell(1, 0).value
            row_flag = 0                         # 初始化指针 即当前写入行是第一行
            for j in range(sheet2.ncols):                 # 写入每一列的名称
                new_sheet.write(row_flag, j, sheet2.cell(head_row, j).value)

        row_flag += 1                            # 转到下一列
        for j in range(sheet2.ncols):
                new_sheet.write(row_flag, j, sheet2.cell(i, j).value)  # 写入每一列的数据

    for fname in workbook_dict:
        workbook_dict[fname].save(fname)         # 保存workbook对象


if __name__ == '__main__':
    sheet_name = 'Sheet3'
    file_name = r'E:\政府性债务投资项目资产清查登记\11.13发单位录系统\附件2-单位账号及密码.xls'
    dir_name = "C:\\Cache\\附件2-"
    read_excel(dir_name=dir_name, file_name=file_name, sheet_name=sheet_name)

