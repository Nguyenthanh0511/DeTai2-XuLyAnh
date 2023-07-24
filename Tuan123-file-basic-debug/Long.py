import pandas as pd
import numpy as np
import time
#trả về value kiểu nguyên thủy
def clean_and_convert_value(value):
    if isinstance(value, str):
        value = value.strip().replace(',', '')
        if value == '':
            return None
        return int(value)
    return value

def searchDropColumn(value):
    return np.where(value.values == False)

def dropValue(value):
    result.loc[value.values[0], ['So_Luong{}'.format(value.name[9:])]] = 0

# def calculationPrice(value):
#     value = pd.Series(value, index=result.filter(like='Thoi_Gian').index)
#     filtered_columns = result.filter(like='Thoi_Diem').apply(lambda y: value >= y).any()
#     selected_columns = filtered_columns[filtered_columns].index[-1]
#     so_luong = result['So_Luong{}'.format(value.name[9:])]
#     gia = result['Gia{}'.format(selected_columns[9:])]
#     mask = pd.to_numeric(so_luong, errors='coerce').notna() & pd.to_numeric(gia, errors='coerce').notna()
#     result.loc[mask, 'Thanh_Tien'] = pd.to_numeric(result.loc[mask, 'Thanh_Tien'], errors='coerce') + pd.to_numeric(so_luong.loc[mask]) * pd.to_numeric(gia.loc[mask])
def calculationPrice(value):
    value = pd.Series(value, index=result.filter(like='Thoi_Gian').index)
    filtered_columns = result.filter(like='Thoi_Diem').apply(lambda y: value >= y).any()
    selected_columns = filtered_columns[filtered_columns].index[-1]
    so_luong = result['So_Luong{}'.format(value.name[9:])]
    gia = result['Gia{}'.format(selected_columns[9:])]
    mask = pd.to_numeric(so_luong, errors='coerce').notna() & pd.to_numeric(gia, errors='coerce').notna()
    result.loc[mask, 'Thanh_Tien'] = pd.to_numeric(result.loc[mask, 'Thanh_Tien'], errors='coerce') + pd.to_numeric(so_luong.loc[mask]) * pd.to_numeric(gia.loc[mask])

start_time = time.time()

data = pd.read_excel('HangHoa_data (1)again.xlsx', sheet_name=None)

data['TongHop'].set_index('Ma_So', drop=False, inplace=True)

tempDonGia = data['DonGia'].rename(columns=lambda x: x.replace('Thoi_Gian', 'Thoi_Diem'))
tempDonGia[tempDonGia.filter(like='Gia').columns] = tempDonGia[tempDonGia.filter(like='Gia').columns].applymap(clean_and_convert_value)

result = pd.concat([data['BanHang'], tempDonGia, data['TongHop']])
result = result.groupby('Ma_So', as_index=False).sum()
result.replace(r'^\s*-+\s*$', 0, regex=True, inplace=True)
result[result.filter(like='So_Luong').columns] = result[result.filter(like='So_Luong').columns].replace('???', None).apply(pd.to_numeric)
result.drop(result.index[-1], inplace=True)
result = result.apply(lambda x: pd.to_datetime(x, errors='coerce') if x.name.startswith('Thoi_Gian') or x.name.startswith('Thoi_Diem') or x.name.startswith('Tu_Ngay') or x.name.startswith('Den_Ngay') else x)

result.filter(like='Thoi_Gian').apply(lambda x: (x >= result['Tu_Ngay']) & (x <= result['Den_Ngay']), axis=0).filter(like='Thoi_Gian').apply(searchDropColumn).filter(like='Thoi_Gian').apply(lambda col: col.apply(lambda x: x.tolist())).filter(like='Thoi_Gian').apply(dropValue)

result['So_Luong'] = result[result.filter(like='So_Luong').columns].sum(axis=1)
result.filter(like='Thoi_Gian').apply(calculationPrice)

data['TongHop']['Ten_Hang'] = data['TongHop']['Ma_So'].map(data['DanhMuc'].set_index('Ma_So', drop=False)['Ten_Hang'])
data['TongHop']['So_Luong'] = data['TongHop']['Ma_So'].map(result.set_index('Ma_So', drop=False)['So_Luong'])
data['TongHop']['Thanh_Tien'] = data['TongHop']['Ma_So'].map(result.set_index('Ma_So', drop=False)['Thanh_Tien'])
data['TongHop'].loc['Tổng số:', 'Thanh_Tien'] = data['TongHop']['Thanh_Tien'].sum()
data['TongHop']['Thanh_Tien'] = data['TongHop']['Thanh_Tien'].apply(lambda x: '{:,}'.format(x))

with pd.ExcelWriter('HangHoa_data (1)again.xlsx') as writer:
    data['DanhMuc'].to_excel(writer, sheet_name='DanhMuc', index=False)
    data['DonGia'].to_excel(writer, sheet_name='DonGia', index=False)
    data['BanHang'].to_excel(writer, sheet_name='BanHang', index=False)
    data['TongHop'].to_excel(writer, sheet_name='TongHop', index=False)

print("--- %s seconds ---" % (time.time() - start_time))
