import pandas as pd
import plotly.express as px

df_330 = pd.read_csv("Logs_disa_test/romraiderlog_330_20250319_082855.csv", encoding = 'unicode_escape')
df_always_open = pd.read_csv("Logs_disa_test/romraiderlog_20250319_081141_todo0.csv", encoding = 'unicode_escape')
df_always_closed = pd.read_csv("Logs_disa_test/romraiderlog_todo1_20250319_081819_todo1.csv", encoding = 'unicode_escape')
df_original = pd.read_csv("Logs_disa_test/romraiderlog_original_20250319_082233_original.csv", encoding = 'unicode_escape')

df_330_1 = df_330[182:236]
df_330_2 = df_330[444:495]
df_always_open_1 = df_always_open[202:257]
df_always_open_2 = df_always_open[470:523]
df_always_closed_1 = df_always_closed[140:202]
df_always_closed_2 = df_always_closed[392:446]
df_original_1 =df_original[152:207]
df_original_2 =df_original[848:902]
df_330_1['disa'] = '330_1'
df_330_2['disa'] = '330_2'
df_always_open_1['disa'] = 'always_open_1'
df_always_open_2['disa'] = 'always_open_2'
df_always_closed_1['disa'] = 'always_closed_1'
df_always_closed_2['disa'] = 'always_closed_2'
df_original_1['disa'] = 'original_1'
df_original_2['disa'] = 'original_2'

df_330_tog = [df_330_1, df_330_2]
df_330_both = pd.concat(df_330_tog)
df_always_open_tog = [df_always_open_1, df_always_open_2]
df_always_open_both = pd.concat(df_always_open_tog)
df_always_closed_tog = [df_always_closed_1, df_always_closed_2]
df_always_closed_both = pd.concat(df_always_closed_tog)
df_original_tog = [df_original_1, df_original_2]
df_original_both = pd.concat(df_original_tog)


#fig1 = px.line(df_330_both, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='330 disa',color='disa')
#fig1.show()
#fig2 = px.line(df_always_open_both, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='alwais open disa',color='disa')
#fig2.show()
#fig3 = px.line(df_always_closed_both, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='alwais closed disa',color='disa')
#fig3.show()
#fig4 = px.line(df_original_both, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='original disa',color='disa')
#fig4.show()


df_run_1_tog = [df_330_1, df_always_open_1, df_always_closed_1, df_original_1]
df_run_1_con = pd.concat(df_run_1_tog)
df_run_2_tog = [df_330_2, df_always_open_2, df_always_closed_2, df_original_2]
df_run_2_con = pd.concat(df_run_2_tog)
fig1 = px.line(df_run_1_con, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='run_1',color='disa')
fig1.show()
fig2 = px.line(df_run_2_con, x = '* Engine Speed (RPM)', y = '* Engine Load (mg/stroke)', title='run_2',color='disa')
fig2.show()



