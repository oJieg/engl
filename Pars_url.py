
import urllib.request

nameV = []  # с именами  groupVerif
nameU = [] # groupUser
nameA = [] # groupAdmin



def next_searth(root_url):
    response = urllib.request.urlopen(root_url)
    htl = str(response.read())
    nameV.clear()
    nameU.clear()
    _pars_htl(htl, "groupVerif")
    _pars_htl(htl, "groupUser")
    _pars_htl(htl, "groupAdmin")





def _pars_htl(htl, group):

    s = htl.find(group)
    htl = htl[s + 20: len(htl)]
    if s != -1:
        _searth_name(htl, group)
        _pars_htl(htl, group)


def _searth_name(htl, group):
    s = htl.find("</a>")
    htlex = htl[0:s]
    s = htlex.rfind(">")
    htlex = htlex[s+1:len(htl)]
    if group == "groupVerif":
        nameV.append(htlex)
    elif group == "groupUser":
        nameU.append(htlex)
    elif group == "groupAdmin":
        nameA.append(htlex)






