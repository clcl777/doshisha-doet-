from bs4 import BeautifulSoup

file = "only_tables.html"

'''
#授業講評削除
for i in range(50):
    with open(file, encoding='utf-8') as f:
        string = f.read()
        string = string.replace('<tr>\n<td><a class="syllabus" href="#" onclick="taihiTopPosition();$(\'#selectedIndex\').val(' + str(i) + ');return doAction(\'form1\',\'goHenkoGamen\');" title="授業講評">授業講評</a></td>\n</tr>','')

    with open(file,encoding='utf-8', mode='w') as f:
        f.write(string)

'''


with open(file, encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    subjects = soup.find_all('tr')
    for subject in subjects:
        td_elements = subject.find_all('td')
        average = td_elements[11].text
        td_elements[11].decompose()  # 平均削除
        new_tag = soup.new_tag('td',class_='average')
        new_tag.string = average
        td_elements[10].insert_after(new_tag)

with open(file, encoding='utf-8', mode='w') as f:
    f.write(str(soup))
