

 NVIDIA GPU Display Driver Security Updates for Multiple Vulnerabilities
==========================================================================================




 Updated 09/29/2021 01:08 PM



NVIDIA GPU display driver vulnerabilities may lead to code execution, denial of service, information disclosure, or escalation of privileges.
---------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](http://www.nvidia.com/product-security/).
-------------------------------------------------------------------------






---




### Vulnerability Details


This section summarizes the potential vulnerabilities. Descriptions use [CWE™](https://cwe.mitre.org/) and risk assessments follow [CVSS](https://www.first.org/cvss/user-guide).


#### CVE-2018-6247


NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer (nvlddmkm.sys) handler for DxgkDdiEscape where a NULL pointer dereference may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.8 
CVSS Temporal Score: 7.9 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2018-6248


NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer handler for DxgkDdiEscape where the software uses a sequential operation to read or write a buffer, but it uses an incorrect length value that causes it to access memory that is outside of the bounds of the buffer which may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.8 
CVSS Temporal Score: 7.9 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2018-6249


NVIDIA GPU Display Driver contains a vulnerability in kernel mode layer handler where a NULL pointer dereference may lead to denial of service or potential escalation of privileges.


CVSS Base Score: 8.8 
CVSS Temporal Score: 7.9 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2018-6250


NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer (nvlddmkm.sys) handler for DxgkDdiEscape where a NULL pointer dereference occurs, which may lead to denial of service or possible escalation of privileges.


CVSS Base Score: 8.2 
CVSS Temporal Score: 7.1 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H/E:U/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H/E:U/RL:O/RC:C)


#### CVE-2018-6251


NVIDIA Windows GPU Display Driver contains a vulnerability in the DirectX 10 Usermode driver, where a specially crafted pixel shader can cause writing to unallocated memory, leading to denial of service or potential code execution.


CVSS Base Score: 7.0 
CVSS Temporal Score: 6.3 
CVSS Vector: CVSS:3.0/[AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H/E:P/RL:O/RC:C)


#### CVE-2018-6252


NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer handler for DxgkDdiEscape where the software allows an actor access to restricted functionality that is unnecessary for production usage, and which may result in denial of service.


CVSS Base Score: 6.5 
CVSS Temporal Score: 5.9 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H/E:P/RL:O/RC:C)


#### CVE-2018-6253


NVIDIA GPU Display Driver contains a vulnerability in the DirectX and OpenGL Usermode drivers where a specially crafted pixel shader can cause infinite recursion leading to denial of service.


CVSS Base Score: 5.5 
CVSS Temporal Score: 5.0 
CVSS Vector: CVSS:3.0/[AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H/E:P/RL:O/RC:C](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H/E:P/RL:O/RC:C)


*NVIDIA’s risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration. NVIDIA doesn’t know of any exploits of these issues at this time.*


### Affected Software


The following software is impacted by the issues described in this bulletin.




Affected Software
| \*\*CVEs\*\* | \*\*Software Products\*\* | \*\*Operating Systems\*\* |
| --- | --- | --- |
| CVE-2018-6247 CVE-2018-6248 CVE-2018-6249 CVE-2018-6250 CVE-2018-6251 CVE-2018-6252 | GeForce Quadro NVS Tesla | Windows |
| CVE-2018-6249 CVE-2018-6253 | GeForce Quadro NVS Tesla | Windows Linux FreeBSD Solaris |


**Notes:**


* For available security updates, see [Software Security Updates](#software-security-updates).
* The table may not be a comprehensive list of all impacted software versions or driver branches and may be updated as more information becomes available. For the latest information, check for updates to this bulletin or go to [NVIDIA Product Security](https://www.nvidia.com/en-us/product-security/) to subscribe to security bulletin notifications.
* Support may have expired for certain software versions or driver branches. Check the [Windows legacy GPU releases](http://nvidia.custhelp.com/app/answers/detail/a_id/3473) and [UNIX legacy GPU releases](http://nvidia.custhelp.com/app/answers/detail/a_id/3142) or contact [NVIDIA Support](http://www.nvidia.com/object/support.html) with any questions.


### Software Security Updates


The following supported software versions contain the security updates for the issues described in this bulletin. If you are using an unsupported software version or an earlier driver branch that is no longer supported, upgrade to one of the updated supported versions listed.


#### Windows




Windows
| \*\*Product\*\* | \*\*Product Series\*\* | \*\*OS\*\* | \*\*Driver Branch\*\* | \*\*Updated Versions\*\* |
| --- | --- | --- | --- | --- |
| GeForce | All | Windows | R390 | 391.35 including HD Audio 1.3.36.6 |
| Quadro, NVS | All | Windows | R390 | 391.33 including HD Audio 1.3.36.6 |
| R384 | 386.28 including HD Audio 1.3.36.6 |
| Tesla | All | Windows | R390 | 391.29 including HD Audio 1.3.36.6 |
| R384 | 386.28 including HD Audio 1.3.36.6 |


#### Linux




Linux
| \*\*Product\*\* | \*\*Product Series\*\* | \*\*OS\*\* | \*\*Driver Branch\*\* | \*\*Updated Versions\*\* |
| --- | --- | --- | --- | --- |
| GeForce | All | Linux, FreeBSD, Solaris | R390 | 390.48 |
| --- | --- | --- | --- | --- |
| R384 | 384.130 |
| Quadro, NVS | All | Linux, FreeBSD, Solaris | R390 | 390.48 |
| R384 | 384.130 |
| Tesla | All | Linux | R390 | 390.46 |
| R384 | 384.125 |


#### Notes


* Download GPU fixes from the [NVIDIA Driver Downloads](http://www.nvidia.com/Download/index.aspx) page.
* If you are an Enterprise Services customer using DGX-1 or DGX Station, visit the [NVIDIA Support Enterprise Services](https://nvid.nvidia.com/enterpriselogin) portal for guidance.
* Your computer hardware vendor may provide you with security updates in a driver version not listed in the tables above. If so, check the vendor's security bulletin to determine which driver versions from the vendor contain the security updates.


### Mitigations


None.


### Acknowledgements


CVE-2018-6251: NVIDIA thanks Piotr Bania of Cisco Talos for reporting this issue to NVIDIA PSIRT.


CVE-2018-6253: NVIDIA thanks the member of Cisco Talos for reporting this issue to NVIDIA PSIRT.


### Get the Most Up to Date Product Security Information


To learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT), see the current list of NVIDIA security bulletins, or subscribe to security bulletin notifications, go to [NVIDIA Product Security](http://www.nvidia.com/product-security/).


### **Revision History**







| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 2.2 | April 26, 2018 | Further clarified the note about driver versions not listed in this bulletin provided by hardware vendors |
| 2.1 | April 24, 2018 | Clarified the note about driver versions not listed in this bulletin provided by hardware vendors |
| 2.0 | April 16, 2018 | Added a note about driver versions not listed in this bulletin provided by hardware vendors |
| 1.0 | March 28, 2018 | Initial release |


### Frequently Asked Questions (FAQs)


#### How do I know what driver version I have installed?


1. Launch Windows Device Manager.
2. Select **Display Adapters**.
3. Select the **NVIDIA GPU** node and right-click.
4. Go to the **Driver** tab.


The driver version can be deciphered as shown in the following examples: 10.18.13.6472 is 364.72 and 10.18.13.472 is 304.72


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA SHIELD TV Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4631/related/1)
* [ NVIDIA GPU Display driver contains multiple vulnerabilities in the kernel mode layer handler](/app/answers/detail/a_id/4462/related/1)
* [ Multiple vulnerabilities in the NVIDIA Windows GPU Display Driver kernel mode layer (nvlddmkm.sys) handler for DxgkDdiEscape and a vulnerability in the Linux GPU Display Driver kernel mode layer (nvidia.ko)](/app/answers/detail/a_id/4278/related/1)
* [ NVIDIA Shield TV and Tablet contain multiple vulnerabilities](/app/answers/detail/a_id/4548/related/1)
* [ NVIDIA Driver Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4611/related/1)








