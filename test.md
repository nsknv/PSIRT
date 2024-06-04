Security Bulletin: Triton Inference Server \- May 2024

__Answer ID: 5546__

NVIDIA has released a software update for NVIDIA Triton Inference Server to address the issues disclosed in this bulletin\. To protect your system, install the latest release from the [Triton Inference Server Releases](https://github.com/triton-inference-server/server/releases) page on GitHub, and view the [Secure Deployment Considerations Guide](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md)\.  


Go to [NVIDIA Product Security](https://www.nvidia.com/security/)\.

### <a id="_60160f8pqm65"></a>Details

This section provides a summary of the potential vulnerabilities that this security update addresses and their impact\. The descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3\.1](https://www.first.org/cvss/v3.1/user-guide) standards\.

__CVE ID__

__Description__

__Vector__

__Base Score__

__Severity__

__CWE__

__Impacts__

CVE\-2024\-0103

[4607386](https://nvbugspro.nvidia.com/bug/4607386)

\(dupe: 4629688\)

NVIDIA Triton Inference Server for Linux and Windows contains a vulnerability where a user may cause an incorrect initialization of a resource by network issue\. A successful exploit of this vulnerability may lead to information disclosure\.

[AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N&version=3.1)

5\.4

Medium

[CWE\-1419](https://cwe.mitre.org/data/definitions/1419.html)

Information disclosure

CVE\-2024\-0095

[4492806](https://nvbugspro.nvidia.com/bug/4492806)

NVIDIA Triton Inference Server for Linux and Windows contains a vulnerability where a user can inject forged logs and executable commands by injecting arbitrary data as a new log entry\. A successful exploit of this vulnerability might lead to data tampering\.

[AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:N&version=3.1)

4\.3

Medium

[CWE\-117](https://cwe.mitre.org/data/definitions/117.html)

Data tampering

The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation\. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration\.   


### <a id="_30j0zll"></a>Security Updates

The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update\.   


__CVE IDs Addressed__

__Affected Products__

__Platform or OS__

__Affected Versions__

__Updated Version __

CVE\-2024\-0095

[4492806](https://nvbugspro.nvidia.com/bug/4492806)

NVIDIA Triton Inference Server

Linux, Windows

20\.10 to 24\.04

24\.05

CVE\-2024\-0103

[4607386](https://nvbugspro.nvidia.com/bug/4607386)

NVIDIA Triton Inference Server

Linux, Windows

 23\.10 to 24\.04

24\.05

### <a id="_w03qlf9maheg"></a>

#### <a id="_be6ts04o2mu5"></a>Notes

- Users deploying NVIDIA Triton Inference Server in production settings should follow the [Secure Deployment Considerations Guide](https://github.com/triton-inference-server/server/blob/main/docs/customization_guide/deploy.md) and ensure that logging and shared memory APIs are protected for use by authorized users\. 

### <a id="_jur6ekiiljxj"></a>Acknowledgements

NVIDIA thanks the following individuals for reporting these issues:

CVE\-2024\-0095: pinkdraconian

CVE\-2024\-0103: Andrew Innes, Will Williams, Jamie Dougherty, Markus Hennerbichler

### <a id="_3znysh7"></a>Get the Most Up\-to\-Date Product Security Information

Visit the[ NVIDIA Product Security](https://www.nvidia.com/security) page to

- Subscribe to security bulletin notifications
- See the current list of NVIDIA security bulletins 
- Report a potential security issue in any NVIDIA supported product
- Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team \(PSIRT\) 

### <a id="_2et92p0"></a>Revision History

__Revision__

__Date__

__Description__

 1\.0

May 24, 2024

 Initial release

### <a id="_tyjcwt"></a>Support

If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html)\.

##### <a id="_3dy6vkm"></a>__Disclaimer__

ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS \(TOGETHER AND SEPARATELY, “MATERIALS”\) ARE BEING PROVIDED “AS IS\.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON\-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW\.

Information is believed to be accurate and reliable at the time it is furnished\. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use\. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation\. Specifications mentioned in this publication are subject to change without notice\. This publication supersedes and replaces all information previously supplied\. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation\.

