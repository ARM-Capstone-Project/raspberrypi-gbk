# AWS IoT Greengrass v2 - Getting Started

https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started.html

![getting started](aws-iot-greengrass/images/1_getting_started.png)

## End Goal

![greengrass core devices](aws-iot-greengrass/getting-started/images/2_greengrass_core_devices.png)

![greengrass deployments](aws-iot-greengrass/images/2b_greengrass_deployments.png)

![s3 bucket](aws-iot-greengrass/getting-started/images/3_s3_bucket.png)

## Set up your environment

Install Java in Raspberry Pi

![java](aws-iot-greengrass/getting-started/images/4_install_java.png)

Install AWS in Raspberry Pi

```shell
$ curl -O 'https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip'
$ unzip awscli-exe-linux-aarch64.zip
$ sudo ./aws/install
$ /usr/local/bin/aws --version
$ aws --version
```

## Install the AWS IoT Greengrass Core software in Raspberry Pi

![download nucleus](aws-iot-greengrass/getting-started/images/5_download_nucleus.png)

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

![install nucleus](aws-iot-greengrass/getting-started/images/6_install_nucleus.png)

![verify greengrass](aws-iot-greengrass/images/7_verify_greengrass_cli.png)

## Develop and test a component on your device

![develop component](aws-iot-greengrass/images/8_develop_component.png)

![deploy component](aws-iot-greengrass/images/9_deploy_component.png)

![restart component](aws-iot-greengrass/images/10_restart_component.png)

![update config](aws-iot-greengrass/images/11_update_config.png)

![remove component](aws-iot-greengrass/images/11b_remove_component.png)

## Create your component in the AWS IoT Greengrass service

Create s3 bucket

![s3 bucket](aws-iot-greengrass/images/12_create_s3_bucket.png)

Create policy

```shell
aws iam create-policy --policy-name BengGreengrassV2ComponentArtifactPolicy --policy-document file://component-artifact-policy.json
```

![create policy](aws-iot-greengrass/images/13. create policy.png)

```shell
aws iam attach-role-policy --role-name GreengrassV2TokenExchangeRole --policy-arn arn:aws:iam::{arn}:policy/BengGreengrassV2ComponentArtifactPolicy
```

![upload artifact to s3](aws-iot-greengrass/images/14_upload_artifact_to_s3.png)

![describe component](aws-iot-greengrass/images/15_describe_component.png)

## Deploy your component

```shell
aws greengrassv2 create-deployment \
  --target-arn "arn:aws:iot:region:arn:thing BengGreengrassCore" \
  --cli-input-json file://hello-world-deployment.json \
  --region ap-southeast-1
```
![tail log](aws-iot-greengrass/images/16_tail_log.png)