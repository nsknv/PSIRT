

 NVIDIA GPU Display Driver - June 2020
========================================================




 Updated 10/05/2021 11:14 AM



NVIDIA has released a software security update for NVIDIA GPU Display Driver. This update addresses issues that may lead to denial of service, escalation of privileges, or information disclosure.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


To protect your system, download and install this software update through the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx) page or, for the vGPU software update, through the NVIDIA Licensing Portal.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).
------------------------------------------------------------------






---




### Details


This section provides a summary of potential vulnerabilities and their impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS](https://www.first.org/cvss/user-guide) v3.0 standards.


#### NVIDIA GPU Display Driver




This section provides a summary of potential vulnerabilities and their impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS](https://www.first.org/cvss/user-guide) v3.0 standards.
| \*\*CVE-ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2020‑5962 | NVIDIA GPU Display Driver contains a vulnerability in the NVIDIA Control Panel component, in which an attacker with local system access can corrupt a system file, which may lead to denial of service or escalation of privileges. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5963 | NVIDIA CUDA Driver contains a vulnerability in the Inter Process Communication APIs, in which improper access control may lead to code execution, denial of service, or information disclosure. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5964 | NVIDIA GPU Display Driver contains a vulnerability in the service host component, in which the application resources integrity check may be missed. Such an attack may lead to code execution, denial of service or information disclosure. | 6.5 | [AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:R/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5965 | NVIDIA GPU Display Driver contains a vulnerability in the DirectX 11 user mode driver (`nvwgf2um/x.dll`), in which a specially crafted shader can cause an out of bounds access, leading to denial of service. | 5.5 | [AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |
| CVE‑2020‑5966 | NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer (`nvlddmkm.sys`) handler for `DxgkDdiEscape`, in which a `NULL` pointer is dereferenced, leading to denial of service or potential escalation of privileges. | 5.5 | [AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |
| CVE‑2020‑5967 | NVIDIA Linux GPU Display Driver contains a vulnerability in the UVM driver, in which a race condition may lead to a denial of service. | 5.5 | [AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |


#### NVIDIA vGPU Software




NVIDIA vGPU Software
| \*\*CVE-ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2020‑5968 | NVIDIA Virtual GPU Manager contains a vulnerability in the vGPU plugin, in which the software does not restrict or incorrectly restricts operations within the boundaries of a resource that is accessed by using an index or pointer, such as memory or files, which may lead to code execution, denial of service, escalation of privileges, or information disclosure. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5969 | NVIDIA Virtual GPU Manager contains a vulnerability in the vGPU plugin, in which it validates a shared resource before using it, creating a race condition which may lead to denial of service or information disclosure. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5970 | NVIDIA Virtual GPU Manager contains a vulnerability in the vGPU plugin, in which an input data size is not validated, which may lead to tampering or denial of service. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5971 | NVIDIA Virtual GPU Manager contains a vulnerability in the vGPU plugin, in which the software reads from a buffer by using buffer access mechanisms such as indexes or pointers that reference memory locations after the targeted buffer, which may lead to code execution, denial of service, escalation of privileges, or information disclosure. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2020‑5972 | NVIDIA Virtual GPU Manager contains a vulnerability in the vGPU plugin, in which local pointer variables are not initialized and may be freed later, which may lead to tampering or denial of service. | 5.5 | [AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H) |
| CVE‑2020‑5973 | NVIDIA Virtual GPU Manager and the guest drivers contain a vulnerability in vGPU plugin, in which there is the potential to execute privileged operations, which may lead to denial of service. | 4.4 | [AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:H) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates for NVIDIA GPU Display Driver


The following table lists the NVIDIA software products affected, versions affected, and the updated version available from nvidia.com that includes this security update. Download the updates from the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx) page.


#### Windows




The following table lists the NVIDIA software products affected, versions affected, and the updated version available from nvidia.com that includes this security update. Download the updates from the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx) page.
| \*\*CVE-IDs Addressed\*\* | \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Driver Branch\*\* | \*\*Affected Versions\*\* | \*\*Updated Versions\*\* |
| --- | --- | --- | --- | --- | --- |
| CVE‑2020‑5962 CVE‑2020‑5963 CVE‑2020‑5964 CVE‑2020‑5965 CVE‑2020‑5966 | GeForce | Windows | R450 | All versions prior to 451.48 | 451.48 |
| Quadro, NVS | Windows | R450 | All versions prior to 451.48 | 451.48 |
| R440 | All versions prior to 443.18 | 443.18 |
| R418 | All versions prior to 426.78 | 426.78 |
| R390 | All versions prior to 392.61 | 392.61 |
| Tesla | Windows | R450 | All versions prior to 451.48 | 451.48 |
| R440 | All versions prior to 443.18 | 443.18 |
| R418 | All versions prior to 426.78 | 426.78 |


#### Linux




Linux
| \*\*CVE-IDs Addressed\*\* | \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Driver Branch\*\* | \*\*Affected Versions\*\* | \*\*Updated Versions\*\* |
| --- | --- | --- | --- | --- | --- |
| CVE‑2020‑5963 CVE‑2020‑5967 | GeForce, Quadro, NVS | Linux | R450 | All versions prior to 450.51 | 450.51 |
| R440 | All versions prior to 440.100 | 440.100 |
| R390 | All versions prior to 390.138 | 390.138 |
| Tesla | Linux | R450 | All versions prior to 450.51.05 | 450.51.05 |
| R440 | All versions prior to 440.95.01 | 440.95.01 |
| R418 | All versions prior to 418.152.00 | 418.152.00 |


Notes:


* Your computer hardware vendor may provide you with Windows GPU display driver versions including 451.55, 446.06 and 443.18 which also contain the security updates.
* The table above may not be a comprehensive list of all affected supported versions or branch releases and may be updated as more information becomes available.
* Earlier software branch releases that support these products are also affected. If you are using an earlier branch release, upgrade to the latest branch release.


### Security Updates for NVIDIA vGPU Software


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update. Log in to the [NVIDIA Enterprise Application Hub](https://nvid.nvidia.com/dashboard/) to download updates from the NVIDIA Licensing Portal.




The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update. Log in to the [NVIDIA Enterprise Application Hub](https://nvid.nvidia.com/dashboard/) to download updates from the NVIDIA Licensing Portal.
| \*\*CVE-IDs Addressed\*\* | \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Affected Versions\*\* | | \*\*Updated Version\*\* | |
| --- | --- | --- | --- | --- | --- | --- |
| \*\*vGPU Software\*\* | \*\*Driver\*\* | \*\*vGPU Software\*\* | \*\*Driver\*\* |
| CVE‑2020‑5973 | vGPU software (guest driver) | Windows | 10.2 | 443.05 | 10.3 | 443.46 |
| 10.1 | 442.06 |
| 10.0 | 441.66 |
| 9.3 | 432.33 | 9.4 | 432.44 |
| 9.2 | 432.08 |
| 9.1 | 431.79 |
| 9.0 | 431.02 |
| 8.3 | 426.52 | 8.4 | 426.72 |
| 8.2 | 426.26 |
| 8.1 | 426.04 |
| 8.0 | 425.31 |
| CVE‑2020‑5973 | vGPU software (guest driver) | Linux | 10.2 | 440.87 | 10.3 | 440.107 |
| 10.1 | 440.56 |
| 10.0 | 440.43 |
| 9.3 | 430.83 | 9.4 | 430.99 |
| 9.2 | 430.63 |
| 9.1 | 430.46 |
| 9.0 | 430.30 |
| 8.3 | 418.130 | 8.4 | 418.149 |
| 8.2 | 418.109 |
| 8.1 | 418.92 |
| 8.0 | 418.70 |
| CVE‑2020‑5968 CVE‑2020‑5969 CVE‑2020‑5970 CVE‑2020‑5971 CVE‑2020‑5972 CVE‑2020‑5973 | vGPU software (Virtual GPU Manager) | Citrix Hypervisor, VMware vSphere, Red Hat Enterprise Linux with KVM, Nutanix AHV | 10.2 | 440.87 | 10.3 | 440.107 |
| 10.1 | 440.53 |
| 10.0 | 440.43 |
| 9.3 | 430.83 | 9.4 | 430.99 |
| 9.2 | 430.67 |
| 9.1 | 430.46 |
| 9.0 | 430.27 |
| 8.3 | 418.130 | 8.4 | 418.149 |
| 8.2 | 418.109 |
| 8.1 | 418.92 |
| 8.0 | 418.66 |


Notes:


* NVIDIA vGPU software 11.0 is not affected.
* The table above may not be a comprehensive list of all affected supported versions or branch releases and may be updated as more information becomes available.
* Earlier software branch releases that support these products are also affected. If you are using an earlier branch release, upgrade to the latest branch release.


### Mitigations


See [Security Updates for NVIDIA GPU Display Driver](#security-updates-display-driver) or [Security Updates for NVIDIA vGPU Software](#security-updates-vgpu-software) for the version to install.


### Acknowledgements


NVIDIA thanks the following people for reporting the issues to us:


CVE‑2020‑5962:


* Eviatar Gerzi, CyberArk Labs
* Nuttakorn Tungpoonsup, Secure D Center Research Team, Secure D Center Co., Ltd.
* Ammarit Thongthua, Secure D Center Research Team, Secure D Center Co., Ltd.
* Sittikorn Sangrattanapitak, Cybersecurity Researcher


CVE‑2020‑5963: Thomas E. Carroll


CVE‑2020‑5965: Piotr Bania of Cisco Talos


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History




Revision History





| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 4.0 | July 16, 2020 | Added information about driver updates for vGPU software 10.3 and a note that vGPU software 11.0 is not affected |
| 3.0 | July 7, 2020 | Added information about the Tesla R450 driver updates for Windows and Linux |
| 2.0 | June 29, 2020 | Updated the availability of R450 Tesla drivers and R440 drivers for vGPU software 10.x Updated the Security Updates table for Linux drivers to include R440 and R390 drivers for GeForce |
| 1.0 | June 24, 2020 | Initial release |


### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


### Frequently Asked Questions (FAQs)


[How do I determine which NVIDIA display driver version is currently installed on my PC?](https://nvidia.custhelp.com/app/answers/detail/a_id/2039)


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, "MATERIALS") ARE BEING PROVIDED "AS IS." NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GPU Display Driver - August 2019](/app/answers/detail/a_id/4841/related/1)
* [ NVIDIA GPU Display Driver - February 2020](/app/answers/detail/a_id/4996/related/1)
* [ NVIDIA GPU Display Driver - November 2019](/app/answers/detail/a_id/4907/related/1)
* [ NVIDIA GPU Display Driver - February 2019](/app/answers/detail/a_id/4772/related/1)
* [ NVIDIA GPU Display Driver - April 2021](/app/answers/detail/a_id/5172/related/1)








