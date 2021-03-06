from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from polls.views import home, login
from Auth.views import V_Login, V_CheckAuth,V_ClearSession
from EmployeeCard.views import V_EmployeeCardIndex,V_GetEmployeeCardData,V_EmployeeCardEdit,V_EmployeeCardSave
from Term.views import V_TermIndex,V_GetTermData,V_TermEdit
from Penalty.views import V_PenaltyIndex,V_GetPenaltyData,V_PenaltyEdit,V_PenaltyNew
from FeeItem.views import V_FeeItemIndex,V_GetFeeItemData,V_FeeItemEdit,V_FeeItemNew
from Store.views import V_StationIndex,V_GetStationData,V_StationEdit,V_StationNew,V_StoreNew
from Deal.views import V_DealIndex,V_GetDealMasterData,V_GetDealDetailData,V_GetEntryData,V_EntryIndex,V_EntryNew,V_EntryDelete
from Checkout.views import V_GetCheckoutData,V_CheckoutIndex,V_CheckoutNew
from Invoice.views import V_InvoiceIndex,V_GetInvoiceData,V_AddInvoiceData
from ExportExcel.views import V_DayReportIndex,V_MonthReportIndex,V_PenaltyReportIndex,V_FeeItemReportIndex,V_GetPenaltyReport,V_GetFeeItemReport,V_IntervalReportIndex
from KioskUi.views import V_KioskIndex,V_KioskPick,V_Refund,V_GetEmployeeData,V_GetDealList,V_GetDealData,V_SaveDealData,V_RefundDealData,V_PayEntry,V_GetDealLotList,V_PayEntryFinish
from PrintData.views import V_PrintDataIndex,V_GetPrintData,V_EditPrintData,V_NewPrintData,V_GetLastPrintData
from Backup.views import V_BackupIndex,V_DoBackup
from reserve.views import V_ReserveIndex

Auth_urlpatterns = [
    url(r'^login/$', V_Login),
    url(r'^home/$', V_CheckAuth),
    url(r'^clearsession/$', V_ClearSession),
]

EmployeeCard_urlpatterns = [
    path('index/', V_EmployeeCardIndex),
    path('GetEmployeeCardData/', V_GetEmployeeCardData),
    path('Edit/<int:id>/', V_EmployeeCardEdit),
    path('Save/', V_EmployeeCardSave),
]

Term_urlpatterns = [
    path('index/', V_TermIndex),
    path('GetTermData/', V_GetTermData),
    path('Edit/<int:id>', V_TermEdit),
    path('Edit/', V_TermEdit),
]

Penalty_urlpatterns = [
    path('index/', V_PenaltyIndex,name='PenaltyIndex'),
    path('GetPenaltyData/', V_GetPenaltyData),
    #path('PenaltySearch/', V_PenaltySearch,name='PenaltySearch'),
    path('Edit/<int:id>/', V_PenaltyEdit,name='PenaltyEdit'),
    path('Edit/', V_PenaltyNew,name='PenaltyNew'),
]

FeeItem_urlpatterns = [
    path('index/', V_FeeItemIndex,name='FeeItemIndex'),
    path('GetFeeItemData/', V_GetFeeItemData),
    #path('PenaltySearch/', V_PenaltySearch,name='PenaltySearch'),
    path('Edit/<int:id>/', V_FeeItemEdit,name='FeeItemEdit'),
    path('Edit/', V_FeeItemNew,name='FeeItemNew'),
]

Invoice_urlpatterns = [
    path('index/', V_InvoiceIndex),
    path('GetInvoiceData/', V_GetInvoiceData),
    path('AddInvoice/', V_AddInvoiceData),
]

Deal_urlpatterns = [
    path('index/', V_DealIndex),
    path('GetDealMasterData/', V_GetDealMasterData),
    path('GetDealDetailData/', V_GetDealDetailData),
    path('entryindex/', V_EntryIndex,name='EntryIndex'),
    path('GetEntryData/', V_GetEntryData,name='GetEntryData'),
    path('entryedit/', V_EntryNew,name='EntryNew'),
    path('entrydelete/<str:DealDate>/<str:LotNo>/', V_EntryDelete,name='EntryDelete'),
]

Store_urlpatterns = [
    path('index/', V_StationIndex,name='StationIndex'),
    path('GetStationData/', V_GetStationData),
    #path('PenaltySearch/', V_PenaltySearch,name='PenaltySearch'),
    path('StationEdit/<int:id>/', V_StationEdit,name='StationEdit'),
    path('StationEdit/', V_StationNew,name='StationNew'),
    path('StoreEdit/', V_StoreNew,name='StoreNew'),
]

Checkout_urlpatterns = [
    path('index/', V_CheckoutIndex,name='CheckoutIndex'),
    path('GetCheckoutData/', V_GetCheckoutData),
    path('CheckoutNew/', V_CheckoutNew,name='CheckoutNew'),
]

ExportExcel_urlpatterns = [
    path('DayReportIndex/', V_DayReportIndex),
    path('MonthReportIndex/', V_MonthReportIndex),
    path('IntervalReportIndex/', V_IntervalReportIndex),
    path('PenaltyReportIndex/', V_PenaltyReportIndex),
    path('FeeItemReportIndex/', V_FeeItemReportIndex),
    path('GetPenaltyReport/', V_GetPenaltyReport,name='GetPenaltyReport'),
    path('GetFeeItemReport/', V_GetFeeItemReport,name='GetFeeItemReport'),

]
KioskUi_urlpatterns=[
    path('index/', V_KioskIndex),
    path('pick/<int:id>/', V_KioskPick),
    path('Refund/<int:id>/', V_Refund),
    path('PayEntry/<int:id>/', V_PayEntry),
    path('GetEmployee/<str:CardNo>/', V_GetEmployeeData),
    path('GetDealList/<str:InvoiceNo>/', V_GetDealList),
    path('GetDealLotList/<str:LotNo>/', V_GetDealLotList),
    path('PayEntryFinish/<str:LotNo>/<int:UserID>/', V_PayEntryFinish),
    path('GetDealData/<str:MasterID>/', V_GetDealData),
    path('SaveDealData/<str:PayType>/', V_SaveDealData),
    path('RefundDealData/<str:MasterID>/<int:UserID>/', V_RefundDealData),
]
Backup_urlpatterns=[
    path('index/',V_BackupIndex),
    path('DoBackup/',V_DoBackup),
]
Reserve_urlpatterns=[
    path('index/',V_ReserveIndex,name='ReserveIndex'),
    #path('setzero/',V_ReserveSetzero),
    #path('return/',V_ReserveReturn),
    #path('setmoney/',V_ReserveSetmoney),
]
PrintData_urlpatterns = [
    path('index/', V_PrintDataIndex,name='PrintDataIndex'),
    path('GetPrintData/', V_GetPrintData),
    path('EditPrintData/<int:id>/', V_EditPrintData,name='EditPrintData'),
    path('NewPrintData/', V_NewPrintData,name='NewPrintData'),
    path('GetLastPrintData/', V_GetLastPrintData),
]
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',home),
    url(r'^login/$',login),
    url(r'^polls/', include('polls.urls')),
    url(r'^Auth/', include(Auth_urlpatterns)),
    path('EmployeeCard/', include(EmployeeCard_urlpatterns)),
    path('Term/', include(Term_urlpatterns)),
    path('Penalty/', include(Penalty_urlpatterns)),
    path('FeeItem/', include(FeeItem_urlpatterns)),
    path('Invoice/', include(Invoice_urlpatterns)),
    path('Deal/', include(Deal_urlpatterns)),
    path('Store/', include(Store_urlpatterns)),
    path('Checkout/', include(Checkout_urlpatterns)),
    path('ExportExcel/', include(ExportExcel_urlpatterns)),
    path('KioskUi/', include(KioskUi_urlpatterns)),
    path('Backup/', include(Backup_urlpatterns)),
    path('Reserve/', include(Reserve_urlpatterns)),
    path('PrintData/', include(PrintData_urlpatterns)),
]
