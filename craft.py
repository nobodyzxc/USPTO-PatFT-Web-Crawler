import Patent_Crawler as ptc
import sys, csv
from tqdm import tqdm

# Description

nos = open(sys.argv[1], 'r').read().split()

with open('error.txt', 'w', newline='') as errfile:
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['No.', 'Abstract', 'Claims'])
    
        for no in tqdm(nos):
            try:
                _, PatFT_link, _, _, _ = ptc.PN_str_and_url(no)
                soup = ptc.url2soup(PatFT_link)
                
                abstract = soup.find('b', text='Abstract')\
                                .parent.find_next_siblings('p')[0].string
                
                claims = ''
                claim_switch = False

                for tag in soup.find('center', text='Claims').next_siblings:
                    if tag.name == 'center': break
                    if tag.string: claims += tag.string

                writer.writerow([no, abstract, claims])
            except Exception as e:
                print("{} error: {}".format(no, e))
                errfile.write("{} error: {}\n".format(no, e))
