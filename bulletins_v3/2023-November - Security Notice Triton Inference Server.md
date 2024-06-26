# Security Notice: Triton Inference Server (Bulletin ID: 5493)



Security Notice: Triton Inference Server - November 2023
========================================================




 Updated 12/18/2023 01:10 PM



This notice is regarding Triton Inference Server. 


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### December 4, 2023:


Triton Inference Server is designed for flexibility and allows developers to create and deploy inferencing solutions in various ways.  Triton Inference Server enables teams to deploy any AI model from multiple deep learning and machine learning frameworks, including TensorRT, TensorFlow, PyTorch, ONNX, OpenVINO, Python, RAPIDS FIL, and more.   

  

NVIDIA has developed a [Secure Deployment Considerations Guide](https://github.com/triton-inference-server/server/blob/r23.11/docs/customization_guide/deploy.md) to help our users make knowledgeable decisions that preemptively consider Secure Deployment.  This guide provides best practices that users deploying Triton-based solutions should consider integrating to fortify the setup and deployment of their Model Repository.  


Additionally, NVIDIA made the following items available in the Triton development branch on November 10, 2023, all of which are available in the release branch today, December 4, 2023. 


* Updated software that behaves as follows:
	+ Provides the ability to restrict the HTTP endpoint of the model load API
	+ Prevents the model load API configuration option from accessing directories outside the model directory


The latest release can be installed from the [Triton Inference Server Release](https://github.com/triton-inference-server/server/releases) Github page or the [NGC Triton Inference Server](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver) page.
### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.1 | December 18, 2023 | Release date updated to December 4, 2023 |
| 1.0 | November 30, 2023 | Initial release |


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GPU Display Driver - October 2023](/app/answers/detail/a_id/5491/related/1)
* [ NVIDIA GeForce NOW for Android - August 2023](/app/answers/detail/a_id/5476/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2023](/app/answers/detail/a_id/5466/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023](/app/answers/detail/a_id/5442/related/1)
* [ NVIDIA Omniverse Kit - January 2023](/app/answers/detail/a_id/5418/related/1)








