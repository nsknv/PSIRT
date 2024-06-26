# NVIDIA Cumulus Linux (Bulletin ID: 5480)



 NVIDIA Cumulus Linux - September 2023
========================================================




 Updated 09/11/2023 02:42 PM




NVIDIA has released a software update for NVIDIA Cumulus Linux. This update addresses security issues that may lead to information disclosure and denial of service. To protect your system, download and install the latest version of NVIDIA Cumulus Linux from the [NVIDIA Enterprise Support Portal](https://enterprise-support.nvidia.com/s/).



Go to [NVIDIA Product Security](https://www.nvidia.com/security/).








---




### 


### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.






| \*\*CVE ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector and CWE\*\* |
| --- | --- | --- | --- |
| CVE-2023-25525 | NVIDIA Cumulus Linux contains a vulnerability in forwarding where a VxLAN-encapsulated IPv6 packet received on an SVI interface with DMAC/DIPv6 set to the link-local address of the SVI interface may be incorrectly forwarded. A successful exploit may lead to information disclosure. | 7.5 | [AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) [CWE-284](http://cwe.mitre.org/data/definitions/284.html) |
| CVE-2023-25526 | NVIDIA Cumulus Linux contains a vulnerability in neighmgrd and nlmanager where an attacker on an adjacent network may cause an uncaught exception by injecting a crafted packet. A successful exploit may lead to denial of service. | 6.5 | [AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H) [CWE-248](https://cwe.mitre.org/data/definitions/248.html) |




The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following tables list the NVIDIA systems affected, firmware versions affected, and the updated version that includes this security update.







| \*\*CVE IDs Addressed\*\* | Affected Product | \*\*Operating System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- | --- |
| CVE-2023-25525 | Cumulus Linux | Cumulus Linux | All versions prior to 5.6.0 | 5.6.0 |
| CVE-2023-25526 | Cumulus Linux | Cumulus Linux | All versions prior to 5.5.0 | 5.5.0 |



### Notes


Earlier software branch releases that support this product are also affected. If you are using an earlier branch release, upgrade to the latest branch release.


### 


### Acknowledgements


NVIDIA thanks the following finders:


CVE-2023-25525, CVE-2023-25526: Marc Dovero



### 


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### 


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.0 | September 6, 2023 | Initial release |


### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.












Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GeForce NOW for Android - August 2023](/app/answers/detail/a_id/5476/related/1)
* [ NVIDIA DGX H100 - August 2023](/app/answers/detail/a_id/5473/related/1)
* [ NVIDIA Omniverse Kit - January 2023](/app/answers/detail/a_id/5418/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)
* [ NVIDIA GPU Display Driver - March 2023](/app/answers/detail/a_id/5452/related/1)








