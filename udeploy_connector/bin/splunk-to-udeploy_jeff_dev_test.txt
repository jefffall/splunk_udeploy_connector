# Powershell script to Send Alert to uDeploy
#
#


# Put username / Password here for the uDeploy server


$Credential = (New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "admin",  ("admin" | ConvertTo-SecureString -AsPlainText -Force ))



# uDeploy



$uDeploy_json_string = @'
{
 "application": "Hello Application",
 "applicationProcess": "hello App Process",
 "environment": "helloDeploy",
 "versions": [{
    "version": "1.0",
    "component": "helloWorld"
  }]
}
'@




#[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

#add-type @"
#    using System.Net;
#    using System.Security.Cryptography.X509Certificates;
#   public class TrustAllCertsPolicy : ICertificatePolicy {
#       public bool CheckValidationResult(
#          ServicePoint srvPoint, X509Certificate certificate,
#           WebRequest request, int certificateProblem) {
#           return true;
#       }
#   }
#"@
#[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 



 
add-type @"
    using System.Net;
    using System.Security.Cryptography.X509Certificates;
    public class TrustAllCertsPolicy : ICertificatePolicy {
        public bool CheckValidationResult(
            ServicePoint srvPoint, X509Certificate certificate,
            WebRequest request, int certificateProblem) {
            return true;
        }
    }
"@ 









[System.Net.ServicePointManager]::CertificatePolicy = New-Object TrustAllCertsPolicy 




 #$output = Invoke-WebRequest -Credential $Credential  -Uri "https://udmint.yourcompany.com:8443/cli/applicationProcessRequest/request" -Method POST -Body ($uDeployJson|ConvertTO-Json)  -ContentType "application/json"
 #echo $output


 $response = Invoke-RestMethod  -Credential $Credential -Uri "https://udmint.yourcompany.com:8443/cli/applicationProcessRequest/request" -Method PUT -Body $uDeploy_json_string -ContentType "application/json"
 echo $response

    "Processed Alert"

    #echo  $uDeploy_json_string
