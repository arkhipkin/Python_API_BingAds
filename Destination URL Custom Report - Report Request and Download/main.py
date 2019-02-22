from bingads.v12.reporting import *
from bingads import *
from auth_helper import *



if __name__ == '__main__':
    # You must provide credentials in auth_helper.py.
    # DEVELOPER_TOKEN,  ENVIRONMENT, CLIENT_ID

    FILE_DIRECTORY = os.path.dirname(__file__)
    FILE_NAME = 'bing.csv'
    REPORT_FILE_FORMAT = 'Csv'
    TIMEOUT_IN_MILLISECONDS = 3600000


    authorization_data=AuthorizationData(
        account_id=None,
        customer_id=None,
        developer_token=DEVELOPER_TOKEN,
        authentication=None,
        )


    # You should authenticate for Bing Ads production services with a Microsoft Account.
    authenticate(authorization_data)

    reporting_service_manager=ReportingServiceManager(
        authorization_data=authorization_data,
        poll_interval_in_milliseconds=5000,
        environment=ENVIRONMENT,
        )


    # In addition to ReportingServiceManager, you will need a reporting ServiceClient
    # to build the ReportRequest.

    reporting_service=ServiceClient(
        'ReportingService',
        version=12,
        authorization_data=authorization_data,
        environment=ENVIRONMENT,
        )
    # https://docs.microsoft.com/en-us/bingads/reporting-service/reportrequest?view=bingads-12
    # https://docs.microsoft.com/en-us/bingads/guides/request-download-report?view=bingads-12
    # https://docs.microsoft.com/en-us/bingads/reporting-service/destinationurlperformancereportrequest?view=bingads-12
    # https://docs.microsoft.com/en-us/bingads/reporting-service/reportaggregation?view=bingads-12
    # https://docs.microsoft.com/en-us/bingads/guides/code-example-report-requests?view=bingads-12
    # We need to request report. Ziel-URL type, what means DestinationUrlPerformanceReportRequest
    """<xs:complexType name="DestinationUrlPerformanceReportRequest" xmlns:xs="http://www.w3.org/2001/XMLSchema">
      <xs:complexContent mixed="false">
        <xs:extension base="tns:ReportRequest">
          <xs:sequence>
            <xs:element name="Aggregation" type="tns:ReportAggregation" />
            <xs:element name="Columns" nillable="true" type="tns:ArrayOfDestinationUrlPerformanceReportColumn" />
            <xs:element minOccurs="0" name="Filter" nillable="true" type="tns:DestinationUrlPerformanceReportFilter" />
            <xs:element name="Scope" nillable="true" type="tns:AccountThroughAdGroupReportScope" />
            <xs:element name="Time" nillable="true" type="tns:ReportTime" />
          </xs:sequence>
        </xs:extension>
      </xs:complexContent>
    </xs:complexType>
    """
    #all the different Report Types: https://docs.microsoft.com/en-us/bingads/guides/report-types?view=bingads-12
    report_request = reporting_service.factory.create('DestinationUrlPerformanceReportRequest')
    report_request.ExcludeColumnHeaders = False
    report_request.ExcludeReportFooter = False #None #True
    report_request.ExcludeReportHeader = False
    report_request.Format=REPORT_FILE_FORMAT
    report_request.ReportName='Bing_adgroup_report_BI API'
    #report_request.ReturnOnlyCompleteData=True
    report_request.Aggregation='Daily'
    # ReportLanguage Value Set - Reporting https://docs.microsoft.com/de-de/bingads/reporting-service/reportlanguage?view=bingads-12
    report_request.Language = 'English' # ''German'


    report_time = reporting_service.factory.create('ReportTime')
    # https://docs.microsoft.com/en-us/bingads/reporting-service/reporttime?view=bingads-12
    # You may either use a custom date range or predefined time - https://docs.microsoft.com/en-us/bingads/reporting-service/reporttimeperiod?view=bingads-12
    # custom_date_range_start=reporting_service.factory.create('Date')
    # custom_date_range_start.Day=1
    # custom_date_range_start.Month=1
    # custom_date_range_start.Year=int(strftime("%Y", gmtime()))-1
    # report_time.CustomDateRangeStart=custom_date_range_start
    # custom_date_range_end=reporting_service.factory.create('Date')
    # custom_date_range_end.Day=31
    # custom_date_range_end.Month=12
    # custom_date_range_end.Year=int(strftime("%Y", gmtime()))-1
    # report_time.CustomDateRangeEnd=custom_date_range_end
    # report_time.PredefinedTime=None
    # You may either use a custom date range or predefined time - https://docs.microsoft.com/en-us/bingads/reporting-service/reporttimeperiod?view=bingads-12
    report_time.PredefinedTime = 'Last14Days'
    #https://docs.microsoft.com/en-us/bingads/reporting-service/reporttimezone?view=bingads-12
    report_time.ReportTimeZone = 'AmsterdamBerlinBernRomeStockholmVienna'
    report_request.Time = report_time



    # If you specify a filter, results may differ from data you see in the Bing Ads web application
    #report_filter=reporting_service.factory.create('KeywordPerformanceReportFilter')
    #report_filter.DeviceType=[
    #    'Computer',
    #    'SmartPhone'
    #]
    #report_request.Filter=report_filter


    # Specify the attribute and data report columns.
    # Each of the Report Types contains a subset of attributes and performance statistics
    # all the possible column attributes you can find https://docs.microsoft.com/en-us/bingads/guides/report-attributes-performance-statistics?view=bingads-12
    # https://docs.microsoft.com/en-us/bingads/reporting-service/destinationurlperformancereportcolumn?view=bingads-12 - determine which columns are required and optional for a DestinationUrlPerformanceReportRequest
    # Specify the attribute and data report columns.
    report_columns=reporting_service.factory.create('ArrayOfDestinationUrlPerformanceReportColumn')
    # "Gregorian date","Account name","Campaign name","Campaign ID","Ad group","Ad group ID","Destination URL","Device type","Ad distribution","Impressions","Clicks","Spend","CTR","Average CPC","Avg. position"
    report_columns.DestinationUrlPerformanceReportColumn.append([
        'TimePeriod',
        'AccountName',
        'CampaignName',
        'CampaignId',
        'AdGroupName',
        'AdGroupId',
        'DestinationUrl',
        'DeviceType',
        'AdDistribution',
        'Impressions',
        'Clicks',
        'Spend',
        'Ctr',
        'AverageCpc',
        'AveragePosition',
    ])
    report_request.Columns=report_columns



    # You may optionally sort by any ReportColumn (only in the KeywordPerformanceReport???), and optionally
    # specify the maximum number of rows to return in the sorted report.
    # report_sorts=reporting_service.factory.create('ArrayOfKeywordPerformanceReportSort')
    # report_sort=reporting_service.factory.create('KeywordPerformanceReportSort')
    # # 1st sort column
    # report_sort.SortColumn='CampaignName'
    # report_sort.SortOrder='Ascending'
    # report_sorts.KeywordPerformanceReportSort.append(report_sort)
    # # 1st sort column
    # report_sort.SortColumn='TimePeriod'
    # report_sort.SortOrder='Ascending'
    # report_sorts.KeywordPerformanceReportSort.append(report_sort)
    #
    # report_request.Sort=report_sorts
    # # report_request.MaxRows=10



    reporting_download_parameters = ReportingDownloadParameters(
        report_request=report_request,
        result_file_directory=FILE_DIRECTORY,
        result_file_name=FILE_NAME,
        overwrite_result_file=True,  # Set this value true if you want to overwrite the same file.
        timeout_in_milliseconds=TIMEOUT_IN_MILLISECONDS
        # You may optionally cancel the download after a specified time interval.
    )

    result_file_path = reporting_service_manager.download_file(reporting_download_parameters)
    output_status_message("Download result file: {0}\n".format(result_file_path))