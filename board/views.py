from django.shortcuts import render
from .models import UserBoard

class PaginHelper:
    def __init__(self):
        self.total_pages = 0
        self.totalPageList = 0

    def getTotalPageList(self, total_cnt, rowsPerPage):
        if ((total_cnt % rowsPerPage) == 0):
            self.total_pages = total_cnt / rowsPerPage
            print('getTotalPage #1')
        else:
            self.total_pages = (total_cnt / rowsPerPage) + 1
            print('getTotalPage #2')
        self.totalPageList = []
        for j in range(self.total_pages):
            self.totalPageList.append(j+1)

        return self.totalPageList

rowsPerPage  = 5
def index(request):
    boardList = UserBoard.objects.order_by('-id')[0:5]
    current_page = 1
    totalCnt = UserBoard.objects.all().count()

    paingHelpernIns = PaginHelper()
    totalPageList = paingHelpernIns.getTotalPageList(totalCnt, rowsPerPage)

    return render(request, 'board/listSpecificPage.html', {'boardList': boardList,
                                                           'totalCnt': totalCnt,
                                                           'current_page': current_page,
                                                           'totalPageList': totalPageList})

# Create your views here.
