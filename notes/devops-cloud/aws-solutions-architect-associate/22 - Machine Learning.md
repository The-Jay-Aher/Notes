# Machine Learning

## Quick Summary
- AWS machine learning services range from ready-made AI APIs to full custom model training platforms.
- Amazon SageMaker is the main service for building, training, deploying, and managing custom ML models.
- Services like Rekognition, Comprehend, Translate, Transcribe, Polly, Textract, Forecast, Personalize, and Bedrock provide higher-level capabilities.
- For Solutions Architect questions, focus on selecting the right managed AI/ML service, not on writing ML algorithms.
- Pay attention to data privacy, model hosting, batch vs real-time inference, and integration with S3.

## Machine Learning Levels on AWS
AWS ML services can be grouped into three levels.

| Level | Meaning | Examples |
|---|---|---|
| AI services | Ready-made APIs | Rekognition, Comprehend, Translate, Transcribe |
| ML platform | Build and deploy custom models | SageMaker |
| Infrastructure | Build your own stack | EC2 GPU instances, EKS, ECS |

Most Solutions Architect questions are about choosing the right managed service.

## Amazon SageMaker
Amazon SageMaker is the main AWS service for custom ML.

SageMaker helps with:
- Data preparation.
- Model training.
- Hyperparameter tuning.
- Model deployment.
- Batch transform.
- Model monitoring.
- Feature stores.
- Pipelines.

### SageMaker Workflow
```text
Data in S3 -> train model -> evaluate model -> deploy endpoint or batch job -> monitor
```

### Training
Training creates a model from data.

Inputs:
- Training dataset.
- Algorithm or training script.
- Compute instance type.
- Hyperparameters.
- Output location, usually S3.

### Inference
Inference means using the model to make predictions.

Common options:
- Real-time endpoint: low-latency online predictions.
- Serverless inference: managed scaling for intermittent traffic.
- Asynchronous inference: large payloads or longer processing.
- Batch transform: offline predictions over a dataset.

### Choosing Inference Type
| Requirement | Option |
|---|---|
| User waits for immediate prediction | Real-time endpoint |
| Traffic is intermittent and scaling should be managed | Serverless inference |
| Payload is large or processing takes longer | Asynchronous inference |
| Predict over millions of stored records | Batch transform |

## Amazon Rekognition
Rekognition analyzes images and videos.

Use it for:
- Object detection.
- Scene detection.
- Face detection and comparison.
- Content moderation.
- Text in images.
- Celebrity recognition in supported contexts.

Example:

```text
Image uploaded to S3 -> Lambda -> Rekognition -> store labels in DynamoDB
```

Security note:
- Be careful with face-related features. Follow privacy, consent, and legal requirements.

## Amazon Comprehend
Comprehend is natural language processing for text.

Use it for:
- Sentiment analysis.
- Entity detection.
- Key phrase extraction.
- Language detection.
- Topic modeling.
- Custom classification.

Example:
- Analyze support tickets to detect customer sentiment and route urgent tickets.

## Amazon Translate
Translate provides machine translation.

Use it when:
- Text must be translated between supported languages.
- You need managed translation APIs.
- You want custom terminology support in supported workflows.

Example:
- Translate product descriptions for a global website.

## Amazon Transcribe
Transcribe converts speech to text.

Use it for:
- Call center transcription.
- Meeting notes.
- Subtitle generation.
- Voice analytics pipelines.

Common flow:

```text
Audio in S3 -> Transcribe job -> transcript in S3
```

## Amazon Polly
Polly converts text to speech.

Use it for:
- Voice prompts.
- Accessibility features.
- Audio versions of text content.

## Amazon Textract
Textract extracts text and structured data from documents.

Use it for:
- Forms.
- Tables.
- Scanned documents.
- Invoices.
- Receipts.

Textract is more document-aware than simple OCR.

## Amazon Forecast
Forecast is for time-series forecasting.

Use it for:
- Demand forecasting.
- Inventory planning.
- Traffic forecasts.
- Resource demand prediction.

## Amazon Personalize
Personalize provides recommendation capabilities.

Use it for:
- Product recommendations.
- Content recommendations.
- Personalized ranking.

Example:
- E-commerce recommendations based on user-item interactions.

## Amazon Bedrock
Amazon Bedrock provides access to foundation models through managed APIs.

Use it for:
- Generative AI applications.
- Text generation.
- Summarization.
- Chat assistants.
- Retrieval-augmented generation architectures.

Architectural considerations:
- Keep sensitive data controls clear.
- Use guardrails where appropriate.
- Store knowledge bases in supported vector stores when using RAG patterns.
- Monitor cost and latency.

Because generative AI services evolve quickly, verify current Bedrock model and feature availability in AWS documentation before designing a production system.

## ML Data Storage
S3 is commonly used for ML data.

Why:
- Stores raw datasets.
- Stores processed datasets.
- Stores model artifacts.
- Integrates with SageMaker, Glue, Athena, and many AI services.

Good practices:
- Separate raw, processed, and model artifact prefixes.
- Encrypt data.
- Version important datasets where needed.
- Restrict access with IAM and bucket policies.

## ML Security and Governance
Important controls:
- IAM least privilege.
- KMS encryption for data at rest.
- VPC endpoints/private connectivity where required.
- Data classification.
- CloudTrail audit logs.
- Model artifact access control.
- Input/output data retention policies.

ML systems often process sensitive data, so security is part of the architecture, not an afterthought.

## Batch vs Real-Time ML
| Requirement | Good approach |
|---|---|
| Predict fraud during checkout | Real-time endpoint |
| Score all customers nightly | Batch transform |
| Analyze uploaded videos | Async workflow |
| Translate text on demand | AI service API |
| Build custom recommendation model | SageMaker or Personalize depending on customization |

## Common Exam Clues
| Clue | Likely service |
|---|---|
| Image or video labels | Rekognition |
| Sentiment from text | Comprehend |
| Translate language | Translate |
| Speech to text | Transcribe |
| Text to speech | Polly |
| Extract forms/tables from PDFs | Textract |
| Custom ML lifecycle | SageMaker |
| Product recommendations | Personalize |
| Time series forecast | Forecast |
| Generative AI foundation models | Bedrock |

## Common Mistakes
- Choosing SageMaker when a ready-made AI API solves the requirement.
- Deploying a real-time endpoint for a once-a-day batch job.
- Forgetting that model endpoints need monitoring and cost control.
- Ignoring data privacy and retention.
- Assuming all AWS AI services are available in every Region.
- Storing training data or model artifacts without encryption/access controls.

## Official References
- [Amazon SageMaker documentation](https://docs.aws.amazon.com/sagemaker/)
- [Amazon Rekognition documentation](https://docs.aws.amazon.com/rekognition/)
- [Amazon Comprehend documentation](https://docs.aws.amazon.com/comprehend/)
- [Amazon Translate documentation](https://docs.aws.amazon.com/translate/)
- [Amazon Transcribe documentation](https://docs.aws.amazon.com/transcribe/)
- [Amazon Polly documentation](https://docs.aws.amazon.com/polly/)
- [Amazon Textract documentation](https://docs.aws.amazon.com/textract/)
- [Amazon Forecast documentation](https://docs.aws.amazon.com/forecast/)
- [Amazon Personalize documentation](https://docs.aws.amazon.com/personalize/)
- [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
