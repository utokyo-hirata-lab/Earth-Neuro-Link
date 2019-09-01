from enl_map import locality
lc = locality()

lc.set_default(0,0,3)
#lc.read_spreadsheet('https://docs.google.com/spreadsheets/d/1IUBUV8mGHp9lHNyCOh0FrJTupVpeLQA0W7sl6d7XiWM/edit#gid=1390728700')
lc.auto_collect('1IUBUV8mGHp9lHNyCOh0FrJTupVpeLQA0W7sl6d7XiWM')
#lc.manual_collect('Australia','Pilbara',-21.8097056,117.3049005,'zircon',4.2,'Etc et al., 2019')
#lc.manual_collect('Australia','Pilbara',-23.8097056,119.3049005,'zircon',4.2,'Etc et al., 2018')
#lc.manual_collect('Australia','Pilbara',-24.0097056,118.3000005,'zircon',4.3,'Etc et al., 2017')
#lc.manual_collect('Canada','Labrador',53.682000,-60.746118,'zircon',2.7,'Etc et al., 2016')
#lc.manual_collect('Gabon','Okandja',-0.704010,13.791012,'zircon',2.4,'Etc et al., 2015')

lc.marker('all')
