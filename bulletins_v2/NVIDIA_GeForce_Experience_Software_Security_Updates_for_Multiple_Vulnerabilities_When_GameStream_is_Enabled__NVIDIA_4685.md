

 NVIDIA GeForce Experience Software Security Updates for Multiple Vulnerabilities When GameStream is Enabled
==============================================================================================================================




 Updated 09/29/2021 01:08 PM



NVIDIA GeForce Experience contains vulnerabilities when GameStream is enabled which may lead to escalation of privileges, denial of service, or information disclosure.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](http://www.nvidia.com/product-security/).
-------------------------------------------------------------------------






---




### Vulnerability Details


The following sections summarize the potential vulnerabilities. Descriptions use [CWE](https://cwe.mitre.org/)TM and risk assessments follow the [CVSS](https://www.first.org/cvss/user-guide) V3 standard.


#### CVE-2018-6257


NVIDIA GeForce Experience contains a potential vulnerability when GameStream is enabled where improper access control may lead to a denial of service, escalation of privileges, or both.


CVSS V3 Base Score: 8.8 
CVSS V3 Vector: [AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H/)


#### CVE-2018-6258


NVIDIA GeForce Experience contains a potential vulnerability during GameStream installation where an attacker who has system access can potentially conduct a Man-in-the-Middle (MitM) attack to obtain sensitive information.


CVSS V3 Base Score: 7.7 
CVSS V3 Vector: [AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:L/A:H)


#### CVE-2018-6259


NVIDIA GeForce Experience contains a potential vulnerability when GameStream is enabled, an attacker has system access, and certain system features are enabled, where limited information disclosure may be possible.


CVSS V3 Base Score: 7.3 
CVSS V3 Vector: [AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:L)


*NVIDIA’s risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk of your specific configuration.*


### Affected Software


The following table lists supported software and its affected driver versions. All driver branches prior to the versions listed in the *Affected Versions* column are also impacted by the issues in this bulletin.


| CVEs | Software Product | Operating System | Affected Version |
|:------------------------------------------|:-----------------------|:-------------------|:-----------------------------|
| CVE-2018-6257 CVE-2018-6258 CVE-2018-6259 | GeForce Experience 3.x | Windows | All versions prior to 3.14.1 |
### Software Security Updates


The following table lists the software version containing the security updates for the issues described in this bulletin. If you are using unsupported software versions or earlier driver branches that are no longer supported, upgrade to the updated supported version listed.


| Software Product | Product Series | Operating System | Updated Version |
|:-------------------|:-----------------|:-------------------|:--------------------------|
| GeForce Experience | 3.x | Windows | GeForce Experience 3.14.1 |
Download the updates from the [NVIDIA GeForce Experience Downloads](http://www.geforce.com/geforce-experience/download) page.


### Mitigations


None.


### Acknowledgements


None.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](http://www.nvidia.com/product-security/) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:----------------|:----------------|
| 1 | August 30, 2018 | Initial release |
### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](http://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA Jetson TX1, Jetson TK1, and Tegra K1 L4T Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4616/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [ NVIDIA Driver Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4611/related/1)
* [ NVIDIA GeForce Experience - September 2018](/app/answers/detail/a_id/4725/related/1)
* [ NVIDIA GeForce Experience – March 2019](/app/answers/detail/a_id/4784/related/1)








