

Security Notice: NVIDIA Response to “Rendered Insecure: GPU Side Channel Attacks are Practical” - November 2018
===============================================================================================================




 Updated 09/29/2021 01:09 PM



November 9, 2018
----------------


This notice is a response to the October 2018 publication “Rendered Insecure: GPU Side Channel Attacks are Practical” regarding a software security issue in the NVIDIA GPU Graphics Driver.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


NVIDIA worked closely with the researchers and evaluated the issue following the Coordinated Vulnerability Disclosure process.
------------------------------------------------------------------------------------------------------------------------------


NVIDIA assessed this issue with a base [CVSS V3](https://www.first.org/cvss/user-guide) score of 2.2 (low). NVIDIA will address the issue with a driver release and post a security bulletin on the [NVIDIA Product Security page](https://www.nvidia.com/product-security/).
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------






---




### February 22, 2019 Update


NVIDIA has released updated drivers to address this issue. For more information, see [ NVIDIA GPU Display Driver - February 2019](https://nvidia.custhelp.com/app/answers/detail/a_id/4772).


### Details


| CVE | Description | Base Score | CVSS V3 Vector |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2018‑6260 | NVIDIA graphics driver contains a vulnerability that may allow access to application data processed on the GPU through a side channel exposed by the GPU performance counters. Local user access is required. This is not a network or remote attack vector. | 2.2 | AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:N/A:N |
 


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:------------------|:---------------------------------------------------------------|
| 2 | February 22, 2019 | Added information about updated drivers to address this issue. |
| 1 | November 09, 2018 | Initial release |
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


* [ NVIDIA GPU Display Driver - February 2019](/app/answers/detail/a_id/4772/related/1)
* [Security Notice: NVIDIA Response to Ripple20 - June 2020](/app/answers/detail/a_id/5033/related/1)
* [Security Notice: NVIDIA Response to Cisco Talos Report - July 2020](/app/answers/detail/a_id/5044/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [Security Notice: NVIDIA Response to OpenSSL Vulnerabilities - November 2022](/app/answers/detail/a_id/5405/related/1)








