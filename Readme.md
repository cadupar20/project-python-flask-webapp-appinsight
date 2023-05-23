| Language | Framework | Platform | Author |
| -------- | -------- |--------|--------|
| Python | Flask | Azure Web App, Virtual Machine| |


# Python Flask web application

Sample Python Flask web application built using Visual Studio 2017.

## License:

See [LICENSE](LICENSE).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


# added Python code to use Azure Appplication Insight to collect Telemetry

On requirements.txt file we ran "pip freeze". The most important to comment it was added:
applicationinsights==0.11.10
requests==2.31.0

You have to change on your Website code these files, replace this string for your App Insight Instrumentation Key: example 12345678-123-1234-1234-1234567890123

Layout.html file:
instrumentationKey: "MY_INSTRUMENTATION_KEY"

__init__.py:
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'MY_INSTRUMENTATION_KEY'

Others files modified on the original website example were the following:

* Layout.html
* __init__.py
* views.py
* index.html