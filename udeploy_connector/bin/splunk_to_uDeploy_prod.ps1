 #Param(

 #[parameter(Mandatory=$true)]
 #[alias("-Host")]
 #[string] $hostname,

 #[parameter(Mandatory=$true)]
 #[alias("-Component")]
 #[string] $component, 

 #[parameter(Mandatory=$true)]
 #[alias("-Environment")]
 #[string] $environment,

 #[parameter(Mandatory=$true)]
 #[alias("-Incidentnumber")]
 #[string] $incidentnumber
#)


param(
    [string]$arg1,
    [string]$arg2,
    [string]$arg3,
    [string]$arg4
)



# ", '-Host:', host , '-Component:', component, '-Environment:', environment

$hostname = $arg1
$component = $arg2
$environment = $arg3
$incidentnumber = $arg4






$user = 'userName'
$pass = 'password*'

$pair = "$($user):$($pass)"

#$encodedCreds =[System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($pair))

$basicAuthValue = "Basic $encodedCreds"

$Headers = @{
             Authorization = $basicAuthValue
            }

       $json = '{
                 "application": "AccountService",
                  "applicationProcess": "Restart server",
                  "environment" : $environment
                }'

#$cliUserInfoURL = 'https://udeploy.yourcompany.com/cli/applicationProcessRequest/request'
                #$cliUserInfoResponse = Invoke-RestMethod -Method PUT -Uri $cliUserInfoURL -Headers $Headers -Body $json

echo "Host = " $hostname | Out-File "D:\splunk\var\log\splunk\check_passed_params.txt"
echo "Component = " $component | Add-Content "D:\splunk\var\log\splunk\check_passed_params.txt"
echo "Environment = " $environment  | Add-Content "D:\splunk\var\log\splunk\check_passed_params.txt" 
echo "Incident Number = " $incidentnumber  | Add-Content "D:\splunk\var\log\splunk\check_passed_params.txt" 


 
 
