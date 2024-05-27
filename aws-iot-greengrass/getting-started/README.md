# AWS IoT Greengrass v2 - Getting Started

https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started.html

![getting started](aws-iot-greengrass/images/1. getting started.png)

## End Goal

![greengrass core devices](aws-iot-greengrass/getting-started/images/2. greengrass core devices.png)

![greengrass deployments](aws-iot-greengrass/images/2b. greengrass deployments.png)

![s3 bucket](aws-iot-greengrass/getting-started/images/3. s3 bucket.png)

## Set up your environment

Install Java in Raspberry Pi

![java](aws-iot-greengrass/getting-started/images/4. install java.png)

Install AWS in Raspberry Pi

```shell
$ curl -O 'https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip'
$ unzip awscli-exe-linux-aarch64.zip
$ sudo ./aws/install
$ /usr/local/bin/aws --version
$ aws --version
```

## Install the AWS IoT Greengrass Core software in Raspberry Pi

![download nucleus](aws-iot-greengrass/getting-started/images/5. download nucleus.png)

Install nucleus

```shell
sudo -E java -Droot="/greengrass/v2" -Dlog.store=FILE \
  -jar ./GreengrassInstaller/lib/Greengrass.jar \
  --aws-region ap-southeast-1 \
  --thing-name BengGreengrassCore \
  --thing-group-name BengGreengrassCoreGroup \
  --thing-policy-name GreengrassV2IoTThingPolicy \
  --tes-role-name GreengrassV2TokenExchangeRole \
  --tes-role-alias-name GreengrassCoreTokenExchangeRoleAlias \
  --component-default-user ggc_user:ggc_group \
  --provision true \
  --setup-system-service true \
  --deploy-dev-tools true
```

![install nucleus](aws-iot-greengrass/getting-started/images/6. install nucleus.png)

![verify greengrass](aws-iot-greengrass/images/7. verify greengrass cli.png)

## Develop and test a component on your device

![develop component](aws-iot-greengrass/images/8. develop component.png)

![deploy component](aws-iot-greengrass/images/9. deploy component.png)

![restart component](aws-iot-greengrass/images/10. restart component.png)

![update config](aws-iot-greengrass/images/11. update config.png)

![remove component](aws-iot-greengrass/images/11b. remove component.png)

## Create your component in the AWS IoT Greengrass service

Create s3 bucket


![s3 bucket](aws-iot-greengrass/images/12. create s3 bucket.png)

Create policy

```shell
aws iam create-policy --policy-name BengGreengrassV2ComponentArtifactPolicy --policy-document file://component-artifact-policy.json
```

![create policy](aws-iot-greengrass/images/13. create policy.png)

```shell
aws iam attach-role-policy --role-name GreengrassV2TokenExchangeRole --policy-arn arn:aws:iam::{arn}:policy/BengGreengrassV2ComponentArtifactPolicy
```

![upload artifact to s3](aws-iot-greengrass/images/14. upload artifact to s3 bucket.png)

![describe component](aws-iot-greengrass/images/15. describe component.png)

## Deploy your component

```shell
aws greengrassv2 create-deployment \
  --target-arn "arn:aws:iot:region:arn:thing BengGreengrassCore" \
  --cli-input-json file://hello-world-deployment.json \
  --region ap-southeast-1
```
![tail log](aws-iot-greengrass/images/16. tail log.png)