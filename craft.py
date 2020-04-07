#http://patft.uspto.gov/netacgi/nph-Parser?Sect2=PTO1&Sect2=HITOFF&p=1&u=/netahtml/PTO/search-bool.html&r=1&f=G&l=50&d=PALL&RefSrch=yes&Query=PN/10608886
import Patent_Crawler as ptc
import sys, csv

nos = open(sys.argv[1], 'r').read().split()

with open('output.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['No.', 'Abstract', 'Claims'])


  for no in nos:
      _, PatFT_link, _, _, _ = ptc.PN_str_and_url(no)
      soup = ptc.url2soup(PatFT_link)
      
      abstract = soup.find('b', text='Abstract')\
              .parent.find_next_siblings('p')[0].string
      
      claims = ''
      claim_switch = False

      for tag in soup.find('coma'):
          if tag.name == 'center':
              claim_switch = tag.string == 'Claims'
          if claim_switch and tag.string:
              claims += tag.string

      writer.writerow([no, abstract, claims])
