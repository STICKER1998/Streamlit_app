#%%  streamlit run "C:\Users\TANGZIFENG\Desktop\Credits\pythonProject\daily_report_module.py"
import streamlit as st
import numpy as np
import pandas as pd
import datetime

def adjust_type(ori_data):
    data = []
    for i in range(len(ori_data)):
        if (i not in(4,6)):
            data.append(int(ori_data[i]))
        else:
            data.append(round(float(ori_data[i]),3))
    return data

def final_table(curr_date):
    return pd.DataFrame(np.random.randn(10,3), columns=[f'Col{i}' for i in range(3)])

st.set_page_config(layout="wide")
risk_report = ["日交易情况监控", "商户明细情况" , "商户入网-省份", "发卡机构交易情况-weekly", "交易明细-DE39"]
select_report = st.sidebar.radio("bize_report", risk_report, label_visibility = 'hidden')


if select_report == "日交易情况监控":
    st.header("日交易情况监控")
    now = datetime.datetime.now()
    col1, col2, col3 = st.columns([1,1,2])
    st.divider()
    today = datetime.date.today()
    current_date = col1.date_input("本期日期", (today - datetime.timedelta(days = 1))).strftime("%Y-%m-%d")
    last_date = col2.date_input("上期日期", (today - datetime.timedelta(days = 2))).strftime("%Y-%m-%d")
    st.caption("观察时间: _%s_"%(current_date))

    dict = ["清分交易笔数(total)","清分交易笔数(net)-总体","清分交易笔数(net)-金融类","清分交易笔数(net)-非金融类 ","清分交易金额(net)",
            "清分交易数据-交易类型", "清分交易金额-交易类型", "活卡数-交易", "活卡数-清分", "用户数-清分",
            "入网商户数"]
    dict_num = len(dict)
    data_flag = [""]*4+["￥"]+[""]+["￥"]+[""]*4
    column_num = 5
    row_num = int(np.ceil(dict_num / column_num))
    start_data = np.array([78, 18, 18, 0, 108491.32, 48, 108546.55, 47, 20, 21, 6034865])
    end_data =np.array([69, 15, 13, 2 ,32508.8, 40, 32552.27, 43, 14, 17, 6071663])
    diff_data = end_data - start_data

    end_data = adjust_type(end_data)
    diff_data = adjust_type(diff_data)

    for i in range(row_num):
        st.divider()
        line = st.columns(column_num)
        for j in range(column_num):
            if (i*column_num + j >= dict_num):
                break
            line[j].metric(label = dict[i*column_num + j], value= data_flag[i*column_num + j]+ str(end_data[i*column_num + j]), delta = diff_data[i*column_num + j] )


if select_report == "商户明细情况":
    st.title("商户明细情况")
    st.divider()
    col1, col2, col3 = st.columns([1,1,2])
    st.divider()
    today = datetime.date.today()
    current_date = col1.date_input("本期日期", (today - datetime.timedelta(days = 1))).strftime("%Y-%m-%d")
    df_daily = final_table(current_date)

    st.dataframe(df_daily, use_container_width=True, height=800)

    @st.cache_data

    def convert_df(df):
        return df.to_csv(index =False).encode('utf-8')
    csv = convert_df(df_daily)
    st.download_button(
        label = "Download data as CSV",
        data = csv,
        file_name = "daily_mec_detail_"+ current_date +".csv",
        mime = 'text/csv',
    )

if select_report == "商户入网-省份":
    def get_mec_detail():
        return pd.DataFrame({'省份直辖市':['北京','上海'],'入网商户数':[500,1000]})

    st.title("商户入网-省份")
    df_mec_city = get_mec_detail()
    st.dataframe(df_mec_city, use_container_width=False, height=500)
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index =False).encode('utf-8')
    csv = convert_df(df_mec_city)
    st.download_button(
        label = "Download data as CSV",
        data = csv,
        file_name = "mec_cnt_by_city.csv",
        mime = 'text/csv',
    )

if select_report == "发卡机构交易情况-weekly":
    None
