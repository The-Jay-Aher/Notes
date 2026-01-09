# Terraform Notes

## Read, Generate, Modify Configurations

### Variable Assignment

If I have a `*.tfvars` file with a different name, other than default `terraform` then -

```powershell
terraform plan --var="instance_type=t2.micro"
```

Here the `instance_type` is the name of the variable

### Variable Precedence

Terraform loads variables in the following order, with the later sources taking precedence over the earlier ones:

1. Environment Variables
2. The `terraform.tfvars` file if present
3. The `terraform.tfvars.json` file. if present
4. Any `*.auto.tfvars` or `*.auto.tfvars,json` files, processed in order of their file names
5. Any `-var` or `-var-file` options in the command line

`5` -> Highest Precedence

`1` -> Lowest Precedence

### Data Types in Terraform

-   `string`
-   `number`
-   `bool`
-   `list` -

    -   Allows us to store values for a single variable/argument.
    -   Represented by a pair of square brackets containing a comma-separated sequence of values
    -   Useful when multiple values need to be added for a specific argument
    -   E.g - `["a", 15, true]`

    ```terraform
        variable "my-list" {
            type    = list(string)
            default = ["Mumbai", "Bangalore", "Delhi"]
        }
    ```

-   `set`
-   `map`
    -   A map data type represents a collection of key-value pair elements
-   `null`

### Count Meta-Argument

**Use Case**

-   Sometimes you want to manage several similar objects (like a fixed pool of compute instances) without writing a separate block for each one.

**Count Argument**

-   The count argument accepts a whole number and creates many instances of the resource.

    ```hcl
    resource "aws_instance" "myEC2" {
    ami           = "ami-068e0f1a600cd311c"
    instance_type = "t2.micro"
    count         = 3
    }
    ```

**Challenges with Count**

-   The instances are created through count and identical copies, but you might want to customize certain properties for each one.
-   The exact copy may not be required for many resources and will not work. E.g. - IAM User.

### Introducing Count Index

-   You can also use `count.index` which allows better flexibility. This attribute holds a distinct index number, starting from 0, and uniquely identifies each index created by count meta-argument.

-   `0` -> First EC2 Instance
-   `1` -> Second EC2 Instance
-   `2` -> Third EC2 Instance

**Enhancing with count index**

-   You can use the `count.index` to iterate through the list to have more customization.

### Conditional Expressions

-   Conditional Expression in Terraform allows you to choose between two values based on a condition.

    Syntax -

    ```terraform
    condition ? true_val : false_val
    ```

-   In conditional expressions, when we give no default value to the variable and have `"" ? "t2.micro" : "t2.nano"`, here the output will be `t2.micro`.
-   You can also use conditional expressions with multiple variables. E.g. -
    `instance_type = var.environment == "production" && var.region == "us-east-1" ? "t2.micro" : "t2.nano"`

### Functions

**Introducing Terraform Console**

-   Terraform console provides an interactive environment specifically designed to test functions and experiment with expressions before integrating them into your main code.
-   Command - `terraform console`

_Importance of File Function_

-   File function can reduce the overall Terraform code size by loading contents from external sources during Terraform operations.

    | **Function Categories** | **Functions Available**                  |
    | :---------------------- | ---------------------------------------- |
    | `Numeric Functions`     | abs, ceil, floor, max, min               |
    | `String Functions`      | concat, replace, split, tolower, toupper |
    | `Collection Functions`  | element, keys, length, merge, sort       |
    | `Filesystem Functions`  | file, filebase64, dirname                |

### Local Values

-   Local Values are similar to variables in the sense that they allow you to store data centrally and that can be referenced in multiple parts of the configuration.
-   _Additional Benefits of Locals_ - You can add expressions to locals, which allows you to compute values dynamically.

_Locals v/s Variables_ -

-   Variable value can be defined in a wide variety of places like `terraform.tfvars`, `ENV Variables`, `CLI` and so on.
-   Locals are more of a private resource. You have to directly modify the source code.
-   Locals are used when you want to avoid repeating the same expression multiple times.

_Important Points_ -

-   Local values are often just referred to as `locals`.
-   Local values are created by a `locals` block (plural), but you reference them as attributes on an object `local` (singular).

### Data Sources

-   Data sources allow Terraform to ` use/fetch information outside information of Terraform`.
-   `${path.module}` returns the current file system path where your code is located.
-   A data source is accessed via a special kind of resource known as `data resource`, declared using a data block;
-   Following data block requests that Terraform read from a given data source("aws_instance") and export the result under the given local name("foo").

**Filter Structure** - Within the body(between { and } ) are query constraints defined by the data source.

### Debugging in Terraform

-   Terraform has detailed logs which can be enabled by setting the `TF_LOG` environment variable to any value
-   You can set the `TF_LOG` to one of the log levels `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR` to change the verbosity of the logs
-   `TRACE` is the most verbose and it is the default if `TF_LOG` is set to something other than a log-level name
-   To persist log output you can set `TF_LOG_PATH` to force the log to always be appended to a specific file when logging is enabled

### Load Order & Semantics

-   Terraform generally loads all the configuration files within the directory specified in the alphabetic order.
-   The files loaded must end in either `.tf` or `.tf.json` to specify the format that's in use.

### Dynamic Blocks

-   Dynamic Blocks allow us to dynamically construct repeatable nested blocks which are supported inside resource, data, provider, and provisioner block.

**Iterators** -

-   The iterator argument(optional) sets the name of a temporary variable that represents the current element of the complex value.
-   If omitted, the name of the variable defaults to the label of the dynamic block("ingress" in the above example).

### Terraform Validate

-   `terraform validate` primarily checks whether a configuration is syntactically valid.
-   It can check various aspects including unsupported arguments, undeclared variables and others.

### Terraform Taint

**Understanding Use-Case**

-   Users may have made a lot of manual changes(both infrastructure and inside the server). Two ways to deal with this: Import Changes into Terraform / Delete and Recreate the resource.

**Recreating the resource**

-   The `-replace` option with `terraform apply` to force Terraform to replace an object even though there are no configuration changes that would require it.

_Points to Note_

-   A similar kind of functionality was achieved using the `terraform taint` command in the older versions of Terraform.
-   For Terraform v15.2.0 and later, HashiCorp recommended using the `-replace` option with `terraform apply`.

**Splat Expression**

-   Allows us to get a list of all the attributes.

### Terraform Graph

-   Terraform graph refers to a `visual representation of the dependency relationships` between resources defined in your Terraform configuration.
-   Terraform graphs are a valuable tool for visualization and understanding the relationships between resources in your infrastructure with Terraform.
-   It can improve your overall workflow by aiding in planning, debugging, and managing complex infrastructure configurations.

### Apply from the Plan File

-   Terraform allows you to save a plan to a file.
-   Command - `terraform plan -out ec2.plan`

-   You can run the `terraform apply` by referencing a plan file.
-   This ensures the infrastructure state remains exactly as shown in the plan to ensure consistency.
-   Command - `terraform apply ec2.plan`

_Exploring terraform plan file_

-   You can use the `terraform show` command to read the contents in detail.
-   You can't read the file through File Explorer, since it's a binary file.

_Use-Case of Saving Plan to a File_

-   Many organizations require documented proof of planned changes before implementation.

### Terraform Output

-   The terraform output command is used to extract the value of an output variable from the state file.

### Terraform Settings

-   We can use the provider block to define various aspects of the provider, like region, credentials and so on.
-   _Specific Version to run your code_ - In a Terraform project, your code might require a specific set of versions to run.
-   Terraform settings are used to configure project-specific Terraform behaviours, such as requiring a minimum Terraform version to apply your configuration.
-   Terraform settings are gathered together into `terraform blocks`.

**Use Case**

1. Specifying a required terraform version -
    - If your code is compatible with specific versions of Terraform, you can use the `required_version` block to add your constraints.
2. Specifying Provider Requirements -
    - The `required_providers` block can be used to specify all of the providers required by your terraform code.
3. Flexibility in Settings block -
    - There are vide variety of options that can be specified in the Terraform block.

### Challenges with Larger Infrastructure

-   When you have a larger infrastructure, you will face issues related to API limits for providers.
-   Switch to a smaller configuration where each can be applied independently.
-   1st way -
    -   We can prevent Terraform from querying the current state during operations like `terraform plan`. This can be achieved with the `terraform plan -refresh=false` flag.
-   2nd Way -
    -   Specify the target
    -   The `terraform plan -refresh=false -target=aws_security_group.allow_ssh_conn` flag can be used to target a specific resource.
    -   Generally used as a means to operate on isolated portions of very large configurations.
    -   The `~` sign means that there is an update going on in that place.

### Zipmap Function

-   The zipmap function constructs a map from a list of keys and a corresponding list of values
-   Command - `zipmap(keyslist, valueslist)`
-   **Simple Use Case** -
    -   You are creating multiple IAM users.
    -   You need to output which contains a direct mapping of the IAM names and ARNs.

### Comment in Terraform

-   The terraform language supports 3 different syntaxes for comments:

    |  **Type**   | **Description**                                                                   |
    | :---------: | --------------------------------------------------------------------------------- |
    |     `#`     | begins a single-line comment, ending at the end of the line (recommended over //) |
    |    `//`     | also begins as a single-line comment, as an alternative to #                      |
    | `/_ and _/` | are start and end delimiters for a comment that might span over multiple lines    |

### Resource Behavior and Meta Arguments

-   A `resource block` declares that you want a particular infrastructure object to exist with the given settings.

**How Terraform applies a configuration**

-   Create resources that exist in the configuration but are not associated with a real infrastructure object in the state.
-   Destroy resources that exist in a state but no longer exist in the configuration.
-   Update in-place resources whose arguments have changed.
-   Destroy and re-create resources whose arguments have changed but which cannot be updated in place due to remote API limitations.

**Understanding the Limitations** - Some modifications happened in the Real Infrastructure object that is not part of Terraform but you want to ignore those changes during `terraform apply`. This is where the `meta-argument` comes into the picture.

**Solution - Using Meta Arguments**

-   Terraform allows us to include `meta-argument` within the resource block which allows some details of this standard resource behaviour to be customized on a per-resource basis.

**Different Meta Arguments**

| **Meta-Argument** | **Description**                                                                                                                                         |
| :---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `depends_on`      | Handle hidden resources or module dependencies that Terraform automatically cannot infer                                                                |
| `count`           | Accepts a whole number, and creates that many instances of the resource                                                                                 |
| `for_each`        | Accepts a map or a set of strings, and creates an instance for each item in that map or set                                                             |
| `lifecycle`       | Allows modification to resource lifecycle                                                                                                               |
| `provider`        | Specifies which provider configuration to use for a resource, overriding Terraform's default behaviour of selecting one based on the resource type name |

### Meta-Argument - Lifecycle

**Arguments Available**

| **Arguments**           | **Description**                                                                                                      |
| :---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `create_before_destroy` | A new replacement is created first, and the prior object is destroyed after the replacement is created               |
| `prevent_destroy`       | Terraform to reject with an error any plan that would destroy the infrastructure object associated with the resource |
| `ignore_changes`        | Ignore certain changes to the live resource that does not match the configuration                                    |
| `replace_triggered_by`  | Replaces the resources when any of the referenced items change                                                       |

**Lifecycle Meta-Argument - Create Before Destroy**

-   By default, when Terraform must change a resource argument that cannot be updated in place due to remote API limitations, Terraform will instead destroy the existing object and then create a new replacement object with the new configured arguments.

**Lifecycle Meta-Argument - Prevent Destroy**

-   This meta-argument, when set to true, will cause Terraform to reject with an error any plan that would destroy the infrastructure object associated with the resource, as long as the argument remains present in the configuration.

_Points to Note_

-   This can be used as a measure of safety against the accidental replacement of objects that may be costly to reproduce, such as database instances.
-   Since this argument must be present in the configuration for the protection to apply, note that this setting does not prevent the remote object from being destroyed if the resource block were removed from the configuration entirely.

**Lifecycle Meta-Argument - Ignore Changes**

-   In cases where settings of a remote object is modified by processes outside of Terraform, the Terraform would attempt to "fix" on the run.
-   To change this behaviour and ignore the manually applied change, we can make use of the `ignore_changes` argument under lifecycle.

_Points to Note_

-   Instead of a list, the special keyword `all` may be used to instruct Terraform to ignore all attributes, which means Terraform can create or destroy remote objects but will never propose updates to them.

**Meta-Argument - Count**

-   If your resources are almost identical, the count is appropriate.
-   If distinctive values are needed in the arguments, usage of `for_each` is needed.

### Data Type

**List**

-   Lists are used to store multiple items in a single variable.
-   List items that are ordered, changeable, and allow duplicate values.
-   List items are indexed, the first item has index `[0]`, the second item has index `[1]`, etc.

    ```hcl
    variable "iam_names" {
    type    = list(string)
    default = ["user-01", "user-02", "user-03"]
    }
    ```

**Set**

-   SET is used to store multiple items in a single variable.
-   SET items are unordered and no duplicates are allowed.
-   Command - `demoSet = {"apple", "banana", "mango"}`

_toset Function_ - `toset` function will convert a list of values to set.

### For_Each

-   `for_each` makes use of map/set as an index value of the created resource.

    ```hcl
    resource "aws_iam_user" "iam" {
    for_each = toset(["user-01", "user=02", "user-03"])
    name     = each.key
    }
    ```

**Replication Count Challenge**

-   If a new element is added, it will not affect the other resources.

**The each object**

-   In blocks where `for_each` is set, an additional each object is available.
-   The object has 2 main attributes:

    | **Each Object** | **Description**                                           |
    | :-------------- | --------------------------------------------------------- |
    | `each.key`      | The map key (or set member) corresponding to the instance |
    | `each.value`    | The map value of the corresponding to this instance       |

## Terraform Provisioners

_Not included in current exam syllabus_

### Overview of Provisioners

**Setting the base**

We have been using Terraform to create and manage resources for a specific provider.

Organizations would want end-to-end solutions for creation of infrastructure and configuring appropriate packages required for the application.

**Introducing Provisioners**

-   Provisioners allow you to `execute scripts on a local or remote machine` as a part of resource creation or destruction.

-   Example: After the VM is launched, install the software package required for the application.

### Type of Provisioners

**Setting the Base**

Provisioners are used to `execute scripts on a local or remote machine` as part of resource creation or destruction.

There are 2-major types of provisioners:

1. `local-exec`
2. `remote-exec`
3. `file` - Minor

**Type 1 - local-exec provisioner**

-   The local-exec provisioner invokes a local executable after a resource is created.
-   Example: After the EC2 instance is launched, fetch the `ip` and store it in file `server_ip.txt`

**Type 2 - remote-exec provisioner**

-   `remote-exec` provisioners allow to invoke scripts or run commands directly on the remote server.
-   Example: After EC2 is launched, install "apache" software

### Format of Provisioners

**Defining Provisioners**

-   Provisioners are defined inside a specific resource.
-   Provisioners are defined by `provisioner` followed by the type of provisioner.

**Local Exec Provisioner Approach**

-   For local provisioner, we have to specify the command that needs to be run locally.

**Remote Exec Provisioner Approach**

-   Since commands executed are executed on remote-server, we have to provide a way for Terraform to connect to the remote server.

**Points to Note** -

_Provisioners are Defined inside the Resource Block_

-   It is not necessary to define an `aws_instance` resource block for the provisioner to run.
-   They can also be defined inside other resource types as well.

_Multiple Provisioner Blocks for Single Resources_

-   We can define multiple provisioner blocks in a single resource block.

### Creation-Time and Destroy-Time Provisioners

**Creation-Time Provisioners**

-   By default, provisioners run when the resources are defined within is created.
-   Creation-Time provisioners are `only run during creation`, not during updating or any other lifecycle.

**Destroy-Time Provisioners**

-   Destroy provisioner run before the provisioner is destroyed.
-   Example: Remove and De-link anti-virus software before EC2 get terminated.

**Tainting Resource in Creation-Time Provisioners**

-   If a creation-time provisioner fails, the resource is marked as tainted.
-   A tainted resource will be planned for destruction and recreation upon the next terraform apply.
-   Terraform does this because a failed provisioner can leave a resource in a semi-configured state.

### Failure Behavior for Provisioners

The `on_failure` setting can be used to change the default behaviour.

| **Allowed Values** | **Description**                                                                                                  |
| :----------------- | ---------------------------------------------------------------------------------------------------------------- |
| `continue`         | Ignore the error and continue with the creation or destruction.                                                  |
| `fail`             | Raise an error and stop applying (the default behaviour). If this is a creation provisioner, taint the resource. |

## Terraform Modules

### Basics of Terraform Modules

**Understanding the Basic** -

In software engineering, `don't repeat yourself` (DRY) is a principle of software development aimed at reducing the repetition of software patterns.

**Challenges** -

1. Repetition of code.
2. Change in AWS Provider-specific option will require a change in EC2 code blocks for all the teams.
3. Lack of standardization.
4. Difficulty to manage.
5. Difficult for developers to use.

**Better Approach** -

-   In this approach, the DevOps team has defined a standard Ec2 template in a central location that all can use.

**Introducing Terraform Modules** -

-   Terraform Modules allows us to centralize the resource configuration and it makes it easier for multiple projects to re-use the Terraform code for projects.

Example -

```hcl
module "e2_instance" {
    source = "terraform-aws-modules/ec2-instance/aws"
}
```

**Multiple Modules for a Single Project**

-   Instead of writing code from scratch, we can use multiple ready-made modules available.

### Points to Note -

**Understanding the Base**

For some infrastructure resources, you can directly use the module calling code, and the entire infrastructure will be created for you.

**Avoiding Confusion**

-   Just by referencing any module, it is not always the case that the infrastructure will be created for you directly.
-   Some of the modules require specific inputs and values from the user side to be filled in before a resource gets created.

**Example Module - AWS EKS**

-   If you try to use an AWS EKS Module directly and run `terraform apply`, it will throw an `error`.

**Module Structure can be Different**

-   Some modules in GitHub can contain multiple sets of modules together for different features. In such cases, you have to reference the exact sub-module required.

### Choosing the right Terraform module

**Understanding the Base** -

Terraform registry can contain multiple modules for a specific infrastructure resource maintained by different users.

**1 - Check total downloads**

-   Module downloads can provide an early indication of the level of acceptance by users in the Terraform community.

**2 - Check the GitHub page of the Module**

-   GitHub pages can provide important information related to the contributors, reported issues, and other data.

**3 - Avoid Modules written by individual participants**

-   Avoid module that are maintained by a single contributor as regular updates, issues and other areas might not always be maintained.

**4 - Analyze Module Documentation**

-   Good documentation must include an overview, usage instructions, input and output variables, and examples.

**5 - Check the version history of Module**

-   Look at the version history. Frequent versions and a clear versioning strategy suggest active maintenance.

**6 - Analyze the Code**

-   Inspect the module's source code on GitHub or another platform. Clean, well-structured code is a good sign.

**7 - Check the community feedback**

-   The number of starts and forks on GitHub can indicate the popularity and community interest.

**8 - Modules maintained by the Hashicorp Partner**

-   Search for modules maintained by Hashicorp partners.

**Important Point to Note**

-   Avoid directly trying any random Terraform Module that is not actively maintained and looks shady(primarily by sole individual contributors)
-   An attacker can include malicious code in a module that sends information about the environment to the attacker.

**Which modules do organizations use?**

-   In most scenarios, organizations maintain their own set of modules
-   They might initially fork a module from the Terraform Registry and modify it based on their use case.

### Creating Base Module Structure for custom module

**Understanding the Base**

-   A base `modules` folder.
-   A sub-folder containing the name of each module that is available.

**What is Inside each Sub-Folders**

-   Each module's sub-folder contains the actual module Terraform code that other projects can reference from.

**Calling the Module**

-   Each team can call various set of modules that are available in the modules folder based on their requirements.

**Our Practical Structure**

-   Our practical structure will include two main folders(modules and teams).
-   Modules sub-folder will contain a sub-folder of available modules.
-   Teams sub-folder will contain list of teams that we want to be made available.

### Module Sources - Calling a Module

**Understanding the Base**

Module source code can be present in a wide variety of locations.

These include:

1. GitHub
2. HTTP URLs
3. S3 Buckets
4. Terraform Registry
5. Local Paths

**Base- Calling the Module**

-   To reference the module, you need to make use of the `module` block.
-   The module block must contain the source argument that contains the location of the referenced module.

**Example 1 - Local Paths**

-   Local paths are used to reference to module that is available in the filesystem.
-   A local path must begin with `./` or `../` to indicate that a local path.

**Example 2 - Generic Git Repository**

-   Arbitrary Git repositories can be used by prefixing with the special `git::` prefix.

    ```hcl
        module "vpc" {
            source = "git::https://example.com/vpc.git"
        }
    ```

**Module Version**

-   A specific module can have multiple versions
-   You can reference to specific version of the module with the `version` block.

### Improvements in Custom Module Code

**Our Simple Module**

-   We created a very simple module that allows developers to launch an EC2 instance when calling the module.

**Challenge 1 - Hardcoded Values**

-   The values are hardcoded as part of the module.
-   If the developer is calling the module, he will have to stick with the same values.
-   The developer will not be able to override the hardcoded values of the module.

**Challenge 2 - Provider Improvements**

-   Avoid hard-coding regions in the Module code as much as possible.
-   A `required_provider` block with version control for module to work is important.

### Variables in Terraform Modules

**Convert Hard-Coded values to Variables**

-   For modules, it is especially recommended to convert hard-coded values to `variables` so that they can be overridden based on user requirements.

**Advantages of variables in module code**

-   Variable-based approach allows teams to override the values.

**Reviewing Professional EC2 Module Code**

-   Reviewing an EC2 module code that is professionally written, we see that the values associated with arguments are not hardcoded and variables were used extensively.

### Module Outputs

**Revising Output Values**

-   `Output Values` make information about your infrastructure available on the command line and can expose information for other Terraform configurations to use.

**Understanding the challenge**

-   If you want to create a resource that has a dependency on an infrastructure created through a module, you won't be able to implicitly call it without output values. In simpler terms, we can't get the ID of the instance while it's created, hence we create an output which helps us access the ID of the instance.

**Accessing Child Module Outputs**

-   Ensure that output values in the output code for better flexibility and integration with other resources and projects.

**Revising Output Values**

-   `Output Values` make information about your infrastructure available on the command line and can expose information for other Terraform configurations to use.

**Accessing Child Module Outputs**

-   Ensure to include output values in the middle code for better flexibility and integration with other resources and projects.
-   Format : `module.<MODULE NAME>.<OUTPUT NAME>`

### Root Module v/s Child Module

**Root Module**

-   Root Module resides in the `main working directory of Terraform configuration`. This is the entry point for your infrastructure definition.

**Child Module**

-   A `module that has been called by another module` is often referred to as a child module.

### Standard Module Structure

**Setting the Base**

-   At this stage, we have been keeping the overall module structure very simple to understand the concepts.
-   In production environments, it is important to follow recommendations and best practices set by HashiCorp.

**Basic of Standard Module Structure**

-   The `standard module structure` is a file and directory layout by HashiCorp recommends for re-usable models.

**Planning the Module Structure** -

-   In this scenario, a team of Terraform Producers, who write Terraform code from scratch, will build a collection of modules to provision the infrastructure and applications.
-   The members of the team in charge of the application will consume these modules to provision the infrastructure they need.

**Final Module Output** -

-   After reviewing the consumer team's requirement, the producer team has `broken up the application infrastructure into the following modules`:
    -   Network
    -   Web
    -   App
    -   Database
    -   Routing
    -   Security

### Publishing Modules in Terraform Registry

**Overview of Publishing Modules** -

-   Anyone can publish and share modules on the Terraform Registry.
-   Published modules support versioning, automatic generate documentation, allow browsing version histories, show examples, and READMEs and more.

**Requirement for Publishing Module** -

| **Requirement**             | **Description**                                                                                                                                                              |
| :-------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GitHub`                    | The module must be on GitHub and must be a public repo. This is only a requirement for the public registry.                                                                  |
| `Named`                     | Module repository must use this three-part name format `terraform-<PROVIDER>-<NAME>`.                                                                                        |
| `Repository Description`    | The GitHub repository description is used to populate the short description of the module.                                                                                   |
| `Standard Module Structure` | The module must adhere to the standard module structure.                                                                                                                     |
| `x.y.x tags for releases`   | The registry uses tags to identify module versions. Release tag names must be a semantic version, which can often be prefixed with a `v.`. For example, `v1.0.4` and `0.9.2` |

**Standard Module Structure** -

-   The standard module structure is a file and directory layout that is recommended for reusable modules distributed in separate repositories.
-   There are 2 Primary formats -
    -   Minimal
    -   Complete

### Terraform Workspace

**Setting the Base** -

-   An infrastructure created through Terraform is `tied to the` underlying Terraform configuration in the state file.

**What If?** -

-   What if we have multiple state files for a single Terraform configuration?
-   Can we manage different env's through it separately?

**Introducing Terraform Workspaces** -

-   Terraform workspaces enable us to `manage multiple set of deployments from the same sets of configuration file`.

## Remote State Management

### Terraform and .gitignore

**Overview of gitignore** -

-   The `.gitignore` file is a text file that tells Git which files or folders to ignore in a project.
-   Depending on the environment, it is recommended to avoid committing certain files to GIT.

| **Files to Ignore** | **Description**                                                         |
| :------------------ | ----------------------------------------------------------------------- |
| `.terraform`        | This file will be recreated when terraform init is run.                 |
| `terraform.tfvars`  | Likely to contain secretive data like username/passwords and secrets.   |
| `terraform.tfstate` | Should be stored in the remote site.                                    |
| `crash.log`         | If terraform crashes, the logs are stored in the file named `crash.log` |

### Terraform Backend

**Basics of Backend** -

-   Backends primarily determine where Terraform stores its state.
-   By default, Terraform implicitly uses a backend called local to store state as a local file on disk.

**Challenge with Local Backend** -

-   Nowadays project is handled and collaborated by an entire team.
-   Storing the state file in the local laptop will not allow collaboration.

**Ideal Architecture** -

The following describes one of the recommended architectures -

1. The Terraform code is stored in GIT Repository.
2. The state file is stored in the central backend.

**Backends Supported in Terraform** -

-   Terraform supports multiple backends that allow remote service-related operations.
-   Some of the popular backends include:
    -   S3
    -   Consul
    -   Azurerm
    -   Kubernetes
    -   HTTP
    -   ETCD

**Important Note** -

-   Accessing state in a remote service generally requires some kind of access credentials
-   Some backends act like plain "remote disks" for state files; others support locking the state while operations are being performed, which helps prevent conflict and inconsistencies.

### State Locking

**Understanding State Lock** -

-   Whenever you are performing write operation, terraform will lock the state file.
-   This is very important as otherwise during your ongoing terraform apply operations, if others also try the same it can corrupt your state file.

**Important Note** -

-   State locking happens automatically on all operations that could write state. You won't see any message that it is happening.
-   If state locking fails, terraform will not continue.
-   Not all backends support locking. The documentation of each backend includes details on whether it supports locking or not.

**Force Unlocking State** -

-   Terraform has a `force-unlock` to manually unlock the state if the state locking failed.
-   If you unlock the state when someone else is holding the lock it could cause multiple writers.
-   Force-Unlock should only be used to unlock your lock in the situation where automatic unlocking failed.

### Integrating DynamoDB with S3 for State Locking

**State Locking in S3** -

-   By default, s3 does not support State-Locking functionality
-   You need to make use of the DynamoDB table to achieve state-locking functionality.

### Terraform State Management

**Overview of State Modification** -

-   As your Terraform usage becomes more advanced, there are some cases where you may need to modify the Terraform state.
-   It is important to modify the state file directly. Instead, make use of the Terraform state command.

**Overview of State Modification** -

| **State Sub Command** | **Description**                                               |
| :-------------------- | ------------------------------------------------------------- |
| `list`                | List resources in the terraform state file.                   |
| `mv`                  | Moves item with the terraform state.                          |
| `pull`                | Manually download and output the state from the remote state. |
| `push`                | Manually upload a local state file to a remote state.         |
| `rm`                  | Remove items from the Remote state.                           |
| `show`                | Show the attributes of a single resource in the state.        |

**Sub Command - List** -

-   The `terraform state list` command is used to list resources within a Terraform state.

**Sub Command - Move** -

-   The `terraform state mv` command is used to move items in a Terraform state file.
-   This command is used in many cases in which you want to rename an existing resource without destroying or recreating it.
-   Due to the destructive nature of this command, this command will output a backup copy of the state before saving any changes.
-   Overall Syntax :
    ```hcl
    terraform state mv [options] SOURCE DESTINATION
    ```

**Sub Command - Pull** -

-   The `terraform state pull` command is used to manually download and output the state from remote state,
-   This is useful for reading values out of state (potentially pairing this command with something like jq).

**Sub Command - Push** -

-   The `terraform state push` command is used to manually upload a local file to remote state.
-   This command should rarely be used.

**Sub Command - Remove** -

-   The `terraform state rm` command is used to remove items from the Terraform State.
-   Items removed from the Terraform state are not physically removed.
-   Items removed from the Terraform state are only no longer managed by Terraform.
-   For example, if you remove an AWS instance from the state, the AWS instance will continue running, but the Terraform plan will no longer see that instance.

**Sub Command - Show** -

-   The `terraform state show` command is used to show the attributes of a single resource in the Terraform state.

### Cross-Project Collaboration using Remote State Data source

**Setting up the Base** -

-   In larger enterprises, there can be multiple different teams working on different aspects of an infrastructure resource.

**Understanding the Challenge** -

-   The security team wants all the IP addresses added as part of output values in the tfstate file of the Networking Team project should be whitelisted in the Firewall.

**What needs to be Achieved** -

1. The code from the security team project should connect to the terraform.tfstate file managed by the Networking Intern.
2. The code should fetch all the IP addresses mentioned in the output values in the state file.
3. The code should whitelist these IP addresses in Firewall rules.

### Remote State Data Source

-   The `terraform_remote_state` data source allows us to fetch values from a specified state backend.

### Terraform Import

**Typical Challenge** -

-   It can happen that all the resources in an organization are created manually.
-   The organization now wants to start using Terraform and Manage these resources via Terraform.

**Earlier Approach** -

-   In the older approach, Terraform import would only create the state file associated with the resource running your environment.
-   Users still had to write tf files from scratch.

**Newer Approach** -

-   In the newer approach, `terraform import` can automatically create the terraform configuration files for the resources you want to import.
-   Both the configuration file and the state file will be generated by the command.

**Point to Note** -

-   `Terraform 1.5.0` introduces automatic code generation for imported resources.
-   This dramatically reduces the amount of time you need to spend writing code to match the imported.
-   This feature is not available in the older versions of Terraform.

## Security Primer

### Multiple Provider Configuration

**Understanding the Requirement** -

-   There can be a requirement that multiple resource types in the same TF file need to be delayed in separate regions.

**Setting the Base** -

-   At this stage, we have been dealing with single-provider configuration.

**Alias Meta-Argument** -

-   Each provider can have one default configuration, and `any number of alternate configurations` that include an extra name segment (or `alias`).

### Sensitive Parameter

**Setting the Base** -

-   By default, Terraform will show the values associated with defined attributes in the CLI output during the plan, and apply operations for most of the resources.

**What to Expect** -

-   We should design our Terraform code, in such a way that no sensitive information is available and shown out of the box in CLI Output, Logs, etc.

**Basics of Sensitive Parameter** -

-   Adding sensitive parameters ensures that you do not accidentally expose this data in CLI Output, log output

**Sensitive Values and Output Values** -

-   If you try to reference sensitive value in output value, Terraform will immediately give you an error.
-   If you still want sensitive value content to be available in the "output" of the state file but should not be visible in CLI Output, Logs, the following approach can be used: `sensitive = true`

**Important Point to Note** -

-   Sensitive parameter will NOT protect/redact information from state file.

**Benefits of Mature Providers** -

-   Various providers like AWS will automatically considers the password argument for any database instance as sensitive and will redact it as a sensitive value.

### Overview of HashiCorp Vault

**Let's get started** -

-   HashiCorp Vault allows organizations to secretly store secrets like tokens, passwords, and certificates, along with access management for protecting secrets.
-   One of the common challenges nowadays in an organization is "Secrets Management".
-   Secrets can include database passwords, AWS access/secret keys, API tokens, encryption keys, and others.

### Terraform and Vault Integration

**Vault Provider** -

-   The vault provider allows Terraform to read from, write to, and configure HashiCorp Vault.

**Important Note** -

-   Interacting with a vault from Terraform causes any secrets that you read and write to be persisted in both Terraform's state files.

### Dependency Lock File

**Revising the Basics** -

-   Provider plugins and Terraform are managed independently and have different release cycles.

**Understanding the Challenge** -

-   The AWS code written in Terraform is working perfectly well with AWS Plugin V1.
-   The same code might have some issues with newer AWS plugins.

**Version Dependencies** -

-   Version constraints within the configurations themselves determine the versions of dependencies that are potentially compatible.
-   After selecting a specific version of each dependency Terraform remembers the decisions it made in a dependency lock file so that it can (by default) make the same decisions again in the future.

**Upgrading Option** -

-   If there is a requirement to use a newer or downgrade provider, can override that behaviour by adding the `-upgrade` option when you run `terraform init`, in which case Terraform will disregard the existing selections.

**Points to Note** -

-   When installing a particular provider for the first time, Terraform will pre-populate hashes value with any checksums that are covered by the provider developer's cryptographic signatures, which usually covers all of the available packages for the provider version across all supported platforms.
-   At present, the dependency lock file, tracks only the provider dependencies.
-   Terraform does not remember the version selection for remote modules, so Terraform will always select the newest available module version that meets the specified version constraints.

## Terraform Cloud & Enterprise Capabilities

### Overview of Terraform Cloud

**Overview of Terraform Cloud** -

-   Terraform Cloud manages Terraform runs in a constant and reliable environment with various features like access controls, private registry for sharing modules, policy controls and others.

### Overview of Sentinel

**Overview of Sentinel** -

-   Sentinel is a policy-as-code framework integrated with the HashiCorp Enterprise products.
-   It enables fine-grained, logic-based policy decisions, and can be extended to use information from external sources.
-   Note: Sentinel Policies are a paid feature.

Process:

1. `terraform plan`
2. `sentinel checks`
3. `terraform apply`

### Remote Backend

**Terraform Cloud - Backend Operation Types** -

-   The remote backend stores Terraform state and may be used to run operations in Terraform Cloud.
-   Terraform cloud can also be used with local operations, in which case only the state is stored in the Terraform cloud backend.

**Remote Operations** -

-   When using full remote operations, like terraform plan or terraform apply can be executed in Terraform cloud's run environment, with log output streaming to the local terminal.

### Air-Gapped Environment

**Understanding Concept of Air Gap** -

-   An air gap is a network security measure employed to ensure that a computer network is physically isolated from unsecured networks, such as public Internet.

**Usage of Air-Gapped Systems** -

-   Air-gapped environments are used in various areas. Some of these include:
    -   Military/Governmental Computer Networks/Systems
    -   Financial Computer Systems, such as stock exchanges
    -   Industrial control systems, such as SCADA in Oil & Gas fields.

**Terraform Enterprise Installation Method** -

-   Terraform enterprise installs either using an online or air-gapped method and as the names infer, one requires internet connectivity, the other does not.