# Anthropic User Guides

This document contains all user guides from the Anthropic documentation.

## Table of Contents

1. [Admin API](#admin-api)
2. [Batch processing](#batch-processing)
3. [Building with extended thinking](#building-with-extended-thinking)
4. [Citations](#citations)
5. [Computer use (beta)](#computer-use-(beta))
6. [Context windows](#context-windows)
7. [Create strong empirical evaluations](#create-strong-empirical-evaluations)
8. [Define your success criteria](#define-your-success-criteria)
9. [Embeddings](#embeddings)
10. [Glossary](#glossary)
11. [Google Sheets add-on](#google-sheets-add-on)
12. [Initial setup](#initial-setup)
13. [Initial setup](#initial-setup)
14. [Intro to Claude](#intro-to-claude)
15. [Model Context Protocol (MCP)](#model-context-protocol-(mcp))
16. [Model deprecations](#model-deprecations)
17. [Multilingual support](#multilingual-support)
18. [PDF support](#pdf-support)
19. [Prompt caching](#prompt-caching)
20. [Text generation](#text-generation)
21. [Token counting](#token-counting)
22. [Using the Evaluation Tool](#using-the-evaluation-tool)
23. [Vision](#vision)
24. [Welcome to Claude](#welcome-to-claude)
25. [extended-thinking](#extended-thinking)
26. [models](#models)

---

## Admin API

Source: https://docs.anthropic.com/en/docs/administration/administration-api

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationAdministrationAdmin API[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Administration
# Admin API

The Admin API is unavailable for individual accounts. To collaborate with teammates and add members, set up your organization in Console → Settings → Organization.

The Admin API allows you to programmatically manage your organization’s resources, including organization members, workspaces, and API keys. This provides programmatic control over administrative tasks that would otherwise require manual configuration in the Anthropic Console.

The Admin API requires special access

The Admin API requires a special Admin API key (starting with sk-ant-admin...) that differs from standard API keys. Only organization members with the admin role can provision Admin API keys through the Anthropic Console.

## ​How the Admin API works

When you use the Admin API:

1. You make requests using your Admin API key in the x-api-key header
2. The API allows you to manage:

Organization members and their roles
Organization member invites
Workspaces and their members
API keys

This is useful for:

* Automating user onboarding/offboarding
* Programmatically managing workspace access
* Monitoring and managing API key usage

## ​Organization roles and permissions

There are four organization-level roles.
RolePermissionsuserCan use WorkbenchdeveloperCan use Workbench and manage API keysbillingCan use Workbench and manage billing detailsadminCan do all of the above, plus manage users
## ​Key concepts

### ​Organization Members

You can list organization members, update member roles, and remove members.

### ​Organization Invites

You can invite users to organizations and manage those invites.

### ​Workspaces

Create and manage workspaces to organize your resources:

### ​Workspace Members

Manage user access to specific workspaces:

### ​API Keys

Monitor and manage API keys:

## ​Best practices

To effectively use the Admin API:

* Use meaningful names and descriptions for workspaces and API keys
* Implement proper error handling for failed operations
* Regularly audit member roles and permissions
* Clean up unused workspaces and expired invites
* Monitor API key usage and rotate keys periodically

## ​FAQ

What permissions are needed to use the Admin API?

Only organization members with the admin role can use the Admin API. They must also have a special Admin API key (starting with sk-ant-admin).

Can I create new API keys through the Admin API?

No, new API keys can only be created through the Anthropic Console for security reasons. The Admin API can only manage existing API keys.

What happens to API keys when removing a user?

API keys persist in their current state as they are scoped to the Organization, not to individual users.

Can organization admins be removed via the API?

No, organization members with the admin role cannot be removed via the API for security reasons.

How long do organization invites last?

Organization invites expire after 21 days. There is currently no way to modify this expiration period.

Are there limits on workspaces?

Yes, you can have a maximum of 100 workspaces per Organization. Archived workspaces do not count towards this limit.

What's the Default Workspace?

Every Organization has a “Default Workspace” that cannot be edited or removed, and has no ID. This Workspace does not appear in workspace list endpoints.

How do organization roles affect Workspace access?

Organization admins automatically get the workspace_admin role to all workspaces. Organization billing members automatically get the workspace_billing role. Organization users and developers must be manually added to each workspace.

Which roles can be assigned in workspaces?

Organization users and developers can be assigned workspace_admin, workspace_developer, or workspace_user roles. The workspace_billing role can’t be manually assigned - it’s inherited from having the organization billing role.

Can organization admin or billing members' workspace roles be changed?

Only organization billing members can have their workspace role upgraded to an admin role. Otherwise, organization admins and billing members can’t have their workspace roles changed or be removed from workspaces while they hold those organization roles. Their workspace access must be modified by changing their organization role first.

What happens to workspace access when organization roles change?

If an organization admin or billing member is demoted to user or developer, they lose access to all workspaces except ones where they were manually assigned roles. When users are promoted to admin or billing roles, they gain automatic access to all workspaces.

Was this page helpful?
YesNo[Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)[Glossary](https://docs.anthropic.com/en/docs/resources/glossary)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How the Admin API works
* Organization roles and permissions
* Key concepts
* Organization Members
* Organization Invites
* Workspaces
* Workspace Members
* API Keys
* Best practices
* FAQ


---

## Batch processing

Source: https://docs.anthropic.com/en/docs/build-with-claude/batch-processing

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeBatch processing[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Batch processing

Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing. This pattern is particularly useful when:

* You need to process large volumes of data
* Immediate responses are not required
* You want to optimize for cost efficiency
* You’re running large-scale evaluations or analyses

The Message Batches API is our first implementation of this pattern.

# ​Message Batches API

The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of Messages requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput.

You can explore the API reference directly, in addition to this guide.

## ​How the Message Batches API works

When you send a request to the Message Batches API:

1. The system creates a new Message Batch with the provided Messages requests.
2. The batch is then processed asynchronously, with each request handled independently.
3. You can poll for the status of the batch and retrieve results when processing has ended for all requests.

This is especially useful for bulk operations that don’t require immediate results, such as:

* Large-scale evaluations: Process thousands of test cases efficiently.
* Content moderation: Analyze large volumes of user-generated content asynchronously.
* Data analysis: Generate insights or summaries for large datasets.
* Bulk content generation: Create large amounts of text for various purposes (e.g., product descriptions, article summaries).

### ​Batch limitations

* A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first.
* We process each batch as fast as possible, with most batches completing within 1 hour. You will be able to access batch results when all messages have completed or after 24 hours, whichever comes first. Batches will expire if processing does not complete within 24 hours.
* Batch results are available for 29 days after creation. After that, you may still view the Batch, but its results will no longer be available for download.
* Claude 3.7 Sonnet supports up to 128K output tokens using the extended output capabilities.
* Batches are scoped to a Workspace. You may view all batches—and their results—that were created within the Workspace that your API key belongs to.
* Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See Message Batches API rate limits. Additionally, we may slow down processing based on current demand and your request volume. In that case, you may see more requests expiring after 24 hours.
* Due to high throughput and concurrent processing, batches may go slightly over your Workspace’s configured spend limit.

### ​Supported models

The Message Batches API currently supports:

* Claude 3.7 Sonnet (claude-3-7-sonnet-20250219)
* Claude 3.5 Sonnet (claude-3-5-sonnet-20240620 and claude-3-5-sonnet-20241022)
* Claude 3.5 Haiku (claude-3-5-haiku-20241022)
* Claude 3 Haiku (claude-3-haiku-20240307)
* Claude 3 Opus (claude-3-opus-20240229)

### ​What can be batched

Any request that you can make to the Messages API can be included in a batch. This includes:

* Vision
* Tool use
* System messages
* Multi-turn conversations
* Any beta features

Since each request in the batch is processed independently, you can mix different types of requests within a single batch.

## ​Pricing

The Batches API offers significant cost savings. All usage is charged at 50% of the standard API prices.
ModelBatch InputBatch OutputClaude 3.7 Sonnet$1.50 / MTok$7.50 / MTokClaude 3.5 Sonnet$1.50 / MTok$7.50 / MTokClaude 3 Opus$7.50 / MTok$37.50 / MTokClaude 3.5 Haiku$0.40 / MTok$2 / MTokClaude 3 Haiku$0.125 / MTok$0.625 / MTok
## ​How to use the Message Batches API

### ​Prepare and create your batch

A Message Batch is composed of a list of requests to create a Message. The shape of an individual request is comprised of:

* A unique custom_id for identifying the Messages request
* A params object with the standard Messages API parameters

You can create a batch by passing this list into the requests parameter:

In this example, two separate requests are batched together for asynchronous processing. Each request has a unique custom_id and contains the standard parameters you’d use for a Messages API call.

Test your batch requests with the Messages API

Validation of the params object for each message request is performed asynchronously, and validation errors are returned when processing of the entire batch has ended. You can ensure that you are building your input correctly by verifying your request shape with the Messages API first.

When a batch is first created, the response will have a processing status of in_progress.
JSON
```
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

### ​Tracking your batch

The Message Batch’s processing_status field indicates the stage of processing the batch is in. It starts as in_progress, then updates to ended once all the requests in the batch have finished processing, and results are ready. You can monitor the state of your batch by visiting the Console, or using the retrieval endpoint:

You can poll this endpoint to know when processing has ended.

### ​Retrieving batch results

Once batch processing has ended, each Messages request in the batch will have a result. There are 4 result types:
Result TypeDescription`succeeded`Request was successful. Includes the message result.`errored`Request encountered an error and a message was not created. Possible errors include invalid requests and internal server errors. You will not be billed for these requests.`canceled`User canceled the batch before this request could be sent to the model. You will not be billed for these requests.`expired`Batch reached its 24 hour expiration before this request could be sent to the model. You will not be billed for these requests.
You will see an overview of your results with the batch’s request_counts, which shows how many requests reached each of these four states.

Results of the batch are available for download at the results_url property on the Message Batch, and if the organization permission allows, in the Console. Because of the potentially large size of the results, it’s recommended to stream results back rather than download them all at once.

The results will be in .jsonl format, where each line is a valid JSON object representing the result of a single request in the Message Batch. For each streamed result, you can do something different depending on its custom_id and result type. Here is an example set of results:
.jsonl file
```
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-3-7-sonnet-20250219","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-3-7-sonnet-20250219","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
```

If your result has an error, its result.error will be set to our standard error shape.

Batch results may not match input order

Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the above example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the custom_id field.

### ​Using prompt caching with Message Batches

The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, since batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30% to 98%, depending on their traffic patterns.

To maximize the likelihood of cache hits in your batch requests:

1. Include identical cache_control blocks in every Message request within your batch
2. Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime
3. Structure your requests to share as much cached content as possible

Example of implementing prompt caching in a batch:

In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with cache_control to increase the likelihood of cache hits.

### ​Best practices for effective batching

To get the most out of the Batches API:

* Monitor batch processing status regularly and implement appropriate retry logic for failed requests.
* Use meaningful custom_id values to easily match results with requests, since order is not guaranteed.
* Consider breaking very large datasets into multiple batches for better manageability.
* Dry run a single request shape with the Messages API to avoid validation errors.

### ​Troubleshooting common issues

If experiencing unexpected behavior:

* Verify that the total batch request size doesn’t exceed 256 MB. If the request size is too large, you may get a 413 request_too_large error.
* Check that you’re using supported models for all requests in the batch.
* Ensure each request in the batch has a unique custom_id.
* Ensure that it has been less than 29 days since batch created_at (not processing ended_at) time. If over 29 days have passed, results will no longer be viewable.
* Confirm that the batch has not been canceled.

Note that the failure of one request in a batch does not affect the processing of other requests.

## ​Batch storage and privacy

* Workspace isolation: Batches are isolated within the Workspace they are created in. They can only be accessed by API keys associated with that Workspace, or users with permission to view Workspace batches in the Console.
* Result availability: Batch results are available for 29 days after the batch is created, allowing ample time for retrieval and processing.

## ​FAQ

How long does it take for a batch to process?

Batches may take up to 24 hours for processing, but many will finish sooner. Actual processing time depends on the size of the batch, current demand, and your request volume. It is possible for a batch to expire and not complete within 24 hours.

Is the Batches API available for all models?

See above for the list of supported models.

Can I use the Message Batches API with other API features?

Yes, the Message Batches API supports all features available in the Messages API, including beta features. However, streaming is not supported for batch requests.

How does the Message Batches API affect pricing?

The Message Batches API offers a 50% discount on all usage compared to standard API prices. This applies to input tokens, output tokens, and any special tokens. For more on pricing, visit our pricing page.

Can I update a batch after it's been submitted?

No, once a batch has been submitted, it cannot be modified. If you need to make changes, you should cancel the current batch and submit a new one. Note that cancellation may not take immediate effect.

Are there Message Batches API rate limits and do they interact with the Messages API rate limits?

The Message Batches API has HTTP requests-based rate limits in addition to limits on the number of requests in need of processing. See Message Batches API rate limits. Usage of the Batches API does not affect rate limits in the Messages API.

How do I handle errors in my batch requests?

When you retrieve the results, each request will have a result field indicating whether it succeeded, errored, was canceled, or expired. For errored results, additional error information will be provided. View the error response object in the API reference.

How does the Message Batches API handle privacy and data separation?

The Message Batches API is designed with strong privacy and data separation measures:

1. Batches and their results are isolated within the Workspace in which they were created. This means they can only be accessed by API keys from that same Workspace.
2. Each request within a batch is processed independently, with no data leakage between requests.
3. Results are only available for a limited time (29 days), and follow our data retention policy.
4. Downloading batch results in the Console can be disabled on the organization-level or on a per-workspace basis.

Can I use prompt caching in the Message Batches API?

Yes, it is possible to use prompt caching with Message Batches API. However, because asynchronous batch requests can be processed concurrently and in any order, cache hits are provided on a best-effort basis.

How do I use beta features in the Message Batches API?

Like the Messages API, you can provide the anthropic-beta header or use the top-evel betas field in the SDK:
Python
```
import anthropic

client = anthropic.Anthropic()

message_batch = client.beta.messages.batches.create(
    betas: ["max-tokens-3-5-sonnet-2024-07-15"],
    ...
)
```

Note that because betas are specified only once for the entire batch, all requests within that batch will share the same beta access.

Does the Message Batches API support extended output capabilities with Claude 3.7 sonnet?

Yes, Claude 3.7 Sonnet’s extended output capabilities (up to 128K tokens) are supported in the Message Batches API.

Was this page helpful?
YesNo[Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)[Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Message Batches API
* How the Message Batches API works
* Batch limitations
* Supported models
* What can be batched
* Pricing
* How to use the Message Batches API
* Prepare and create your batch
* Tracking your batch
* Retrieving batch results
* Using prompt caching with Message Batches
* Best practices for effective batching
* Troubleshooting common issues
* Batch storage and privacy
* FAQ


---

## Building with extended thinking

Source: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeBuilding with extended thinking[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Building with extended thinking

Extended thinking gives Claude 3.7 Sonnet enhanced reasoning capabilities for complex tasks, while also providing transparency into its step-by-step thought process before it delivers its final answer.

## ​How extended thinking works

When extended thinking is turned on, Claude creates thinking content blocks where it outputs its internal reasoning. Claude incorporates insights from this reasoning before crafting a final response.

The API response will include both thinking and text content blocks.

In multi-turn conversations, only thinking blocks associated with a tool use session or assistant turn in the last message position are visible to Claude and are billed as input tokens; thinking blocks associated with earlier assistant messages are not visible to Claude during sampling and do not get billed as input tokens.

## ​Implementing extended thinking

Add the thinking parameter and a specified token budget to use for extended thinking to your API request.

The budget_tokens parameter determines the maximum number of tokens Claude is allowed use for its internal reasoning process. Larger budgets can improve response quality by enabling more thorough analysis for complex problems, although Claude may not use the entire budget allocated, especially at ranges above 32K.

Your budget_tokens must always be less than the max_tokens specified.

The API response will include both thinking and text content blocks:

```
{
    "content": [
        {
            "type": "thinking",
            "thinking": "To approach this, let's think about what we know about prime numbers...",
            "signature": "zbbJhbGciOiJFU8zI1NiIsImtakcjsu38219c0.eyJoYXNoIjoiYWJjMTIzIiwiaWFxxxjoxNjE0NTM0NTY3fQ...."
        },
        {
            "type": "text",
            "text": "Yes, there are infinitely many prime numbers such that..."
        }
    ]
}
```

## ​Understanding thinking blocks

Thinking blocks represent Claude’s internal thought process. In order to allow Claude to work through problems with minimal internal restrictions while maintaining our safety standards and our stateless APIs, we have implemented the following:

* Thinking blocks contain a signature field. This field holds a cryptographic token which verifies that the thinking block was generated by Claude, and is verified when thinking blocks are passed back to the API. When streaming responses, the signature is added via a signature_delta inside a content_block_delta event just before the content_block_stop event. It is only strictly necessary to send back thinking blocks when using tool use with extended thinking. Otherwise you can omit thinking blocks from previous turns, or let the API strip them for you if you pass them back.
* Occasionally Claude’s internal reasoning will be flagged by our safety systems. When this occurs, we encrypt some or all of the thinking block and return it to you as a redacted_thinking block. These redacted thinking blocks are decrypted when passed back to the API, allowing Claude to continue its response without losing context.
* thinking and redacted_thinking blocks are returned before the text blocks in the response.

Here’s an example showing both normal and redacted thinking blocks:

```
{
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me analyze this step by step...",
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."
    },
    {
      "type": "redacted_thinking",
      "data": "EmwKAhgBEgy3va3pzix/LafPsn4aDFIT2Xlxh0L5L8rLVyIwxtE3rAFBa8cr3qpP..."
    },
    {
      "type": "text",
      "text": "Based on my analysis..."
    }
  ]
}
```

Seeing redacted thinking blocks in your output is expected behavior. The model can still use this redacted reasoning to inform its responses while maintaining safety guardrails.

If you need to test redacted thinking handling in your application, you can use this special test string as your prompt: ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB

When passing thinking and redacted_thinking blocks back to the API in a multi-turn conversation, you must include the complete unmodified block back to the API for the last assistant turn.

This is critical for maintaining the model’s reasoning flow. We suggest always passing back all thinking blocks to the API. For more details, see the Preserving thinking blocks section below.

Example: Working with redacted thinking blocks

This example demonstrates how to handle redacted_thinking blocks that may appear in responses when Claude’s internal reasoning contains content flagged by safety systems:

### ​Suggestions for handling redacted thinking in production

When building customer-facing applications that use extended thinking:

* Be aware that redacted thinking blocks contain encrypted content that isn’t human-readable
* Consider providing a simple explanation like: “Some of Claude’s internal reasoning has been automatically encrypted for safety reasons. This doesn’t affect the quality of responses.”
* If showing thinking blocks to users, you can filter out redacted blocks while preserving normal thinking blocks
* Be transparent that using extended thinking features may occasionally result in some reasoning being encrypted
* Implement appropriate error handling to gracefully manage redacted thinking without breaking your UI

## ​Streaming extended thinking

When streaming is enabled, you’ll receive thinking content via thinking_delta events. Here’s how to handle streaming with thinking:

Example streaming output:

```
event: message_start
data: {"type": "message_start", "message": {"id": "msg_01...", "type": "message", "role": "assistant", "content": [], "model": "claude-3-7-sonnet-20250219", "stop_reason": null, "stop_sequence": null}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "Let me solve this step by step:\n\n1. First break down 27 * 453"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n2. 453 = 400 + 50 + 3"}}

// Additional thinking deltas...

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "EqQBCgIYAhIM1gbcDa9GJwZA2b3hGgxBdjrkzLoky3dl1pkiMOYds..."}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "27 * 453 = 12,231"}}

// Additional text deltas...

event: content_block_stop
data: {"type": "content_block_stop", "index": 1}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": null}}

event: message_stop
data: {"type": "message_stop"}
```

About streaming behavior with thinking

When using streaming with thinking enabled, you might notice that text sometimes arrives in larger chunks alternating with smaller, token-by-token delivery. This is expected behavior, especially for thinking content.

The streaming system needs to process content in batches for optimal performance, which can result in this “chunky” delivery pattern. We’re continuously working to improve this experience, with future updates focused on making thinking content stream more smoothly.

redacted_thinking blocks will not have any deltas associated and will be sent as a single event.

Example: Streaming with redacted thinking

This will output:

```
event: message_start
data: {"type":"message_start","message":{"id":"msg_018J5iQyrGb5Xgy5CWx3iQFB","type":"message","role":"assistant","model":"claude-3-7-sonnet-20250219","content":[],"stop_reason":null,"stop_sequence":null,"usage":{"input_tokens":92,"cache_creation_input_tokens":0,"cache_read_input_tokens":0,"output_tokens":3}}       }

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"redacted_thinking","data":"EvEBCoYBGAIiQAqN5Z4LumxzafxD2yf2zW+hVm/G2/Am05ChRXkU1Xe2wQLPLo0wnmoaVJI1WTkLpRYJAIz2UjzHblLwkJ59xeAqQNr5EWqMZkOr8yNcpbCO5PssXiUvEjhoaC0IN3qyhE3vumOOS9Qd0Ku4AYTgu8VjP4C6IJHnkuIexa0VrU/cFbISDJjPWOWQlyAx4y5FCRoMk55jLUCR8KCZrKrzIjDR8S3F/pCWlz/JA5RN0uprpWAI75HjgcY2NJkPX3sEC0Ew6fl6YEISNk1XsmzWtj4qGArQlCfAW9l8SDiKbXm0UZ4hQhh2ruPbaw=="}  }

event: ping
data: {"type": "ping"}

event: content_block_stop
data: {"type":"content_block_stop","index":0         }

event: content_block_start
data: {"type":"content_block_start","index":1,"content_block":{"type":"redacted_thinking","data":"EvMBCoYBGAIiQKZ6LAz+dCNWxvz0dmjI0gfqEInA9MLVAtFJTpolzOaIbUs28xuKyXVzEQsPWPvP12gN+hxVJ4mYzWT8DCIAxXIqQHwQZcGASLMxWCfHrUlYfFq0vF8IGhRgQKxpj1zxouNLuKdhpZrcHF9vKODIPCPW8EWD13aI6t+exz/UboOs/ZMSDA8tVDp4vkOEUc7sGBoMbiRhGYMqcmAOhb3nIjC/lewBt2l9P+VpJkV78YQ3LhvNh/q3KfsbGuJ2U+lIMPGf9wnzrRC/6xqdsHPe1B0qGozBPKnbBifhyb7xYyWcEWoi/qW9OdoFl1/w"}            }

event: content_block_stop
data: {"type":"content_block_stop","index":1             }

event: content_block_start
data: {"type":"content_block_start","index":2,"content_block":{"type":"redacted_thinking","data":"Eu8BCoYBGAIiQCXtUNB4QyT//Zww832Q+xjJ0oa7/PQZr74OvbS1+a7cRNywZfYMYGGte3RXXTMa6I0bFJOMmXXckcbLxR/L+msqQLhKGx9Bt2FnLpo7bp/PdMQBDDCo+jkbOctnxBQrHCuYbu33o30qPCh73AZ8O1xXXEZfzfLC0L6RoHzLxQSHN5gSDAxGSY7Ifg073BaUYBoMSWHLVrmZrydEfc7SIjAF1R+fYlyVPFwS4Sac/Dw9caskXNF/p+Yn7RNaW9+v/jL03qsqqvemuqRGltSBfZcqFrowQipxo/ftIkEC47Ua64RzSBIe27E="}   }

event: content_block_stop
data: {"type":"content_block_stop","index":2              }

event: content_block_start
data: {"type":"content_block_start","index":3,"content_block":{"type":"redacted_thinking","data":"Eu8BCoYBGAIiQEgE6WUvQO3d6fPpY3OaA95soqeWgZv/Nyi0X6iywTb5KqvUn9NxWySiZwSFZb+4S8ymtHRO4OBKA7eRWEXcBuQqQNudvV6YSFH5ErwaDME0HaEjtHcuy8SslL6RhLwhEJKGpYCzq7zWupcMBB1g57sR8vh/JwGjr7D9sfX9jmM7EsESDEatCbzVVczyZ0TERRoMenFOToj2qn0Xmh1LIjA1WgxaMqiHhb5T4k/++UCKNMH2SEseLzTlR7uIz20qZUXDWtoVck6wc+x7lSWRKXQqFiLoTO1oG0I/lbPz1n2FgC3MH7683FU="}     }

// Additional events...

event: content_block_start
data: {"type":"content_block_start","index":58,"content_block":{"type":"redacted_thinking","data":"EuoBCoYBGAIiQJ/SxkPAgqxhKok29YrpJHRUJ0OT8ahCHKAwyhmRuUhtdmDX9+mn4gDzKNv3fVpQdB01zEPMzNY3QuTCd+1bdtEqQK6JuKHqdndbwpr81oVWb4wxd1GqF/7Jkw74IlQa27oobX+KuRkopr9Dllt/RDe7Se0sI1IkU7tJIAQCoP46OAwSDF51P09q67xhHlQ3ihoM2aOVlkghq/X0w8NlIjBMNvXYNbjhyrOcIg6kPFn2ed/KK7Cm5prYAtXCwkb4Wr5tUSoSHu9T5hKdJRbr6WsqEc7Lle7FULqMLZGkhqXyc3BA"}        }

event: content_block_stop
data: {"type":"content_block_stop","index":58            }

event: content_block_start
data: {"type":"content_block_start","index":59,"content_block":{"type":"text","text":""}              }

event: content_block_delta
data: {"type":"content_block_delta","index":59,"delta":{"type":"text_delta","text":"I'm"}        }

event: content_block_delta
data: {"type":"content_block_delta","index":59,"delta":{"type":"text_delta","text":" not"}     }

event: content_block_delta
data: {"type":"content_block_delta","index":59,"delta":{"type":"text_delta","text":" sure"}    }

// Additional text deltas...

event: content_block_delta
data: {"type":"content_block_delta","index":59,"delta":{"type":"text_delta","text":" me know what you'"}          }

event: content_block_delta
data: {"type":"content_block_delta","index":59,"delta":{"type":"text_delta","text":"d like assistance with."}   }

event: content_block_stop
data: {"type":"content_block_stop","index":59               }

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"end_turn","stop_sequence":null},"usage":{"output_tokens":184}  }

event: message_stop
data: {"type":"message_stop"          }
```

## ​Important considerations when using extended thinking

Working with the thinking budget: The minimum budget is 1,024 tokens. We suggest starting at the minimum and increasing the thinking budget incrementally to find the optimal range for Claude to perform well for your use case. Higher token counts may allow you to achieve more comprehensive and nuanced reasoning, but there may also be diminishing returns depending on the task.

* The thinking budget is a target rather than a strict limit - actual token usage may vary based on the task.
* Be prepared for potentially longer response times due to the additional processing required for the reasoning process.
* Streaming is required when max_tokens is greater than 21,333.

For thinking budgets above 32K: We recommend using batch processing for workloads where the thinking budget is set above 32K to avoid networking issues. Requests pushing the model to think above 32K tokens causes long running requests that might run up against system timeouts and open connection limits.

Thinking compatibility with other features:

* Thinking isn’t compatible with temperature, top_p, or top_k modifications as well as forced tool use.
* You cannot pre-fill responses when thinking is enabled.
* Changes to the thinking budget invalidate cached prompt prefixes that include messages. However, cached system prompts and tool definitions will continue to work when thinking parameters change.

### ​Pricing and token usage for extended thinking

Extended thinking tokens count towards the context window and are billed as output tokens. Since thinking tokens are treated as normal output tokens, they also count towards your rate limits. Be sure to account for this increased token usage when planning your API usage.

For Claude 3.7 Sonnet, the pricing is:
Token useCostInput tokens$3 / MTokOutput tokens (including thinking tokens)$15 / MTokPrompt caching write$3.75 / MTokPrompt caching read$0.30 / MTok
Batch processing for extended thinking is available at 50% off these prices and often completes in less than 1 hour.

All extended thinking tokens (including redacted thinking tokens) are billed as output tokens and count toward your rate limits.

In multi-turn conversations, thinking blocks associated with earlier assistant messages do not get billed as input tokens.

When extended thinking is enabled, a specialized 28 or 29 token system prompt is automatically included to support this feature.

Example: Previous thinking tokens omitted as input tokens for future turns

This example demonstrates that even though the second message includes the assistant’s complete response with thinking blocks, the token counting API shows that previous thinking tokens don’t contribute to the input token count for the subsequent turn:

This behavior occurs because the Anthropic API automatically strips thinking blocks from previous turns when calculating context usage. This helps optimize token usage while maintaining the benefits of extended thinking.

### ​Extended output capabilities (beta)

Claude 3.7 Sonnet can produce substantially longer responses than previous models with support for up to 128K output tokens (beta)—more than 15x longer than other Claude models. This expanded capability is particularly effective for extended thinking use cases involving complex reasoning, rich code generation, and comprehensive content creation.

This feature can be enabled by passing an anthropic-beta header of output-128k-2025-02-19.

When using extended thinking with longer outputs, you can allocate a larger thinking budget to support more thorough reasoning, while still having ample tokens available for the final response.

We suggest using streaming or batch mode with this extended output capability; for more details see our guidance on network reliability considerations for long requests.

## ​Using extended thinking with prompt caching

Prompt caching with thinking has several important considerations:

Thinking block inclusion in cached prompts

* Thinking is only included when generating an assistant turn and not meant to be cached.
* Previous turn thinking blocks are ignored.
* If thinking becomes disabled, any thinking content passed to the API is simply ignored.

Cache invalidation rules

* Alterations to thinking parameters (enabling/disabling or budget changes) invalidate cache breakpoints set in messages.
* System prompts and tools maintain caching even when thinking parameters change.

### ​Examples of prompt caching with extended thinking

System prompt caching (preserved when thinking changes)

Here is the output of the script (you may see slightly different numbers)

```
First request - establishing cache
First response usage: { cache_creation_input_tokens: 1365, cache_read_input_tokens: 0, input_tokens: 44, output_tokens: 725 }

Second request - same thinking parameters (cache hit expected)
Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1365, input_tokens: 386, output_tokens: 765 }

Third request - different thinking budget (cache hit expected)
Third response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1365, input_tokens: 811, output_tokens: 542 }
```

This example demonstrates that when caching is set up in the system prompt, changing the thinking parameters (budget_tokens increased from 4000 to 8000) does not invalidate the cache. The third request still shows a cache hit with cache_read_input_tokens=1365, proving that system prompt caching is preserved even when thinking parameters change.

Messages caching (invalidated when thinking changes)

Here is the output of the script (you may see slightly different numbers)

```
First request - establishing cache
First response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 17, output_tokens: 700 }

Second request - same thinking parameters (cache hit expected)

Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1370, input_tokens: 303, output_tokens: 874 }

Third request - different thinking budget (cache miss expected)
Third response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 747, output_tokens: 619 }
```

This example demonstrates that when caching is set up in the messages array, changing the thinking parameters (budget_tokens increased from 4000 to 8000) invalidates the cache. The third request shows no cache hit with cache_creation_input_tokens=1370 and cache_read_input_tokens=0, proving that message-based caching is invalidated when thinking parameters change.

## ​Max tokens and context window size with extended thinking

In older Claude models (prior to Claude 3.7 Sonnet), if the sum of prompt tokens and max_tokens exceeded the model’s context window, the system would automatically adjust max_tokens to fit within the context limit. This meant you could set a large max_tokens value and the system would silently reduce it as needed.

With Claude 3.7 Sonnet, max_tokens (which includes your thinking budget when thinking is enabled) is enforced as a strict limit. The system will now return a validation error if prompt tokens + max_tokens exceeds the context window size.

### ​How context window is calculated with extended thinking

When calculating context window usage with thinking enabled, there are some considerations to be aware of:

* Thinking blocks from previous turns are stripped and not counted towards your context window
* Current turn thinking counts towards your max_tokens limit for that turn

The diagram below demonstrates the specialized token management when extended thinking is enabled:



The effective context window is calculated as:

```
context window =
  (current input tokens - previous thinking tokens) +
  (thinking tokens + redacted thinking tokens + text output tokens)
```

We recommend using the token counting API to get accurate token counts for your specific use case, especially when working with multi-turn conversations that include thinking.

You can read through our guide on context windows for a more thorough deep dive.

### ​Managing tokens with extended thinking

Given new context window and max_tokens behavior with extended thinking models like Claude 3.7 Sonnet, you may need to:

* More actively monitor and manage your token usage
* Adjust max_tokens values as your prompt length changes
* Potentially use the token counting endpoints more frequently
* Be aware that previous thinking blocks don’t accumulate in your context window

This change has been made to provide more predictable and transparent behavior, especially as maximum token limits have increased significantly.

## ​Extended thinking with tool use

When using extended thinking with tool use, be aware of the following behavior pattern:

1. First assistant turn: When you send an initial user message, the assistant response will include thinking blocks followed by tool use requests.
2. Tool result turn: When you pass the user message with tool result blocks, the subsequent assistant message will not contain any additional thinking blocks.

To expand here, the normal order of a tool use conversation with thinking follows these steps:

1. User sends initial message
2. Assistant responds with thinking blocks and tool requests
3. User sends message with tool results
4. Assistant responds with either more tool calls or just text (no thinking blocks in this response)
5. If more tools are requested, repeat steps 3-4 until the conversation is complete

This design allows Claude to show its reasoning process before making tool requests, but not repeat the thinking process after receiving tool results. Claude will not output another thinking block until after the next non-tool_result user turn.

The diagram below illustrates the context window token management when combining extended thinking with tool use:



Example: Passing thinking blocks with tool results

Here’s a practical example showing how to preserve thinking blocks when providing tool results:

The API response will include thinking, text, and tool_use blocks:

```
{
    "content": [
        {
            "type": "thinking",
            "thinking": "The user wants to know the current weather in Paris. I have access to a function `get_weather`...",
            "signature": "BDaL4VrbR2Oj0hO4XpJxT28J5TILnCrrUXoKiiNBZW9P+nr8XSj1zuZzAl4egiCCpQNvfyUuFFJP5CncdYZEQPPmLxYsNrcs...."
        },
        {
            "type": "text",
            "text": "I can help you get the current weather information for Paris. Let me check that for you"
        },
        {
            "type": "tool_use",
            "id": "toolu_01CswdEQBMshySk6Y9DFKrfq",
            "name": "get_weather",
            "input": {
                "location": "Paris"
            }
        }
    ]
}
```

Now let’s continue the conversation and use the tool

The API response will now only include text

```
{
    "content": [
        {
            "type": "text",
            "text": "Currently in Paris, the temperature is 88°F (31°C)"
        }
    ]
}
```

### ​Preserving thinking blocks

During tool use, you must pass thinking and redacted_thinking blocks back to the API, and you must include the complete unmodified block back to the API.  This is critical for maintaining the model’s reasoning flow and conversation integrity.

While you can omit thinking and redacted_thinking blocks from prior assistant role turns, we suggest always passing back all thinking blocks to the API for any multi-turn conversation. The API will:

* Automatically filter the provided thinking blocks
* Use the relevant thinking blocks necessary to preserve the model’s reasoning
* Only bill for the input tokens for the blocks shown to Claude

#### ​Why thinking blocks must be preserved

When Claude invokes tools, it is pausing its construction of a response to await external information. When tool results are returned, Claude will continue building that existing response. This necessitates preserving thinking blocks during tool use, for a couple of reasons:

1. Reasoning continuity: The thinking blocks capture Claude’s step-by-step reasoning that led to tool requests. When you post tool results, including the original thinking ensures Claude can continue its reasoning from where it left off.
2. Context maintenance: While tool results appear as user messages in the API structure, they’re part of a continuous reasoning flow. Preserving thinking blocks maintains this conceptual flow across multiple API calls.

Important: When providing thinking or redacted_thinking blocks, the entire sequence of consecutive thinking or redacted_thinking blocks must match the outputs generated by the model during the original request; you cannot rearrange or modify the sequence of these blocks.

## ​Tips for making the best use of extended thinking mode

To get the most out of extended thinking:

1. Set appropriate budgets: Start with larger thinking budgets (16,000+ tokens) for complex tasks and adjust based on your needs.
2. Experiment with thinking token budgets: The model might perform differently at different max thinking budget settings. Increasing max thinking budget can make the model think better/harder, at the tradeoff of increased latency. For critical tasks, consider testing different budget settings to find the optimal balance between quality and performance.
3. You do not need to remove previous thinking blocks yourself: The Anthropic API automatically ignores thinking blocks from previous turns and they are not included when calculating context usage.
4. Monitor token usage: Keep track of thinking token usage to optimize costs and performance.
5. Use extended thinking for particularly complex tasks: Enable thinking for tasks that benefit from step-by-step reasoning like math, coding, and analysis.
6. Account for extended response time: Factor in that generating thinking blocks may increase overall response time.
7. Handle streaming appropriately: When streaming, be prepared to handle both thinking and text content blocks as they arrive.
8. Prompt engineering: Review our extended thinking prompting tips if you want to maximize Claude’s thinking capabilities.

## ​Next steps
[Try the extended thinking cookbookExplore practical examples of thinking in our cookbook.](https://github.com/anthropics/anthropic-cookbook/tree/main/extended_thinking)[Extended thinking prompting tipsLearn prompt engineering best practices for extended thinking.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)
Was this page helpful?
YesNo[Extended thinking tips](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)[Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How extended thinking works
* Implementing extended thinking
* Understanding thinking blocks
* Suggestions for handling redacted thinking in production
* Streaming extended thinking
* Important considerations when using extended thinking
* Pricing and token usage for extended thinking
* Extended output capabilities (beta)
* Using extended thinking with prompt caching
* Examples of prompt caching with extended thinking
* Max tokens and context window size with extended thinking
* How context window is calculated with extended thinking
* Managing tokens with extended thinking
* Extended thinking with tool use
* Preserving thinking blocks
* Why thinking blocks must be preserved
* Tips for making the best use of extended thinking mode
* Next steps


---

## Citations

Source: https://docs.anthropic.com/en/docs/build-with-claude/citations

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeCitations[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Citations

Claude is capable of providing detailed citations when answering questions about documents, helping you track and verify information sources in responses.

The citations feature is currently available on Claude 3.7 Sonnet, Claude 3.5 Sonnet (new) and 3.5 Haiku.

Citations with Claude 3.7 Sonnet

Claude 3.7 Sonnet may be less likely to make citations compared to other Claude models without more explicit instructions from the user. When using citations with Claude 3.7 Sonnet, we recommend including additional instructions in the user turn, like "Use citations to back up your answer." for example.

We’ve also observed that when the model is asked to structure its response, it is unlikely to use citations unless explicitly told to use citations within that format. For example, if the model is asked to use  tags in its response, you should add something like “Always use citations in your answer, even within .”

Please share your feedback and suggestions about the citations feature using this form.

Here’s an example of how to use citations with the Messages API:

Comparison with prompt-based approaches

In comparison with prompt-based citations solutions, the citations feature has the following advantages:

* Cost savings: If your prompt-based approach asks Claude to output direct quotes, you may see cost savings due to the fact that cited_text does not count towards your output tokens.
* Better citation reliability: Because we parse citations into the respective response formats mentioned above and extract cited_text, citation are guaranteed to contain valid pointers to the provided documents.
* Improved citation quality: In our evals, we found the citations feature to be significantly more likely to cite the most relevant quotes from documents as compared to purely prompt-based approaches.

## ​How citations work

Integrate citations with Claude in these steps:
1
Provide document(s) and enable citations

* Include documents in any of the supported formats: PDFs, plain text, or custom content documents
* Set citations.enabled=true on each of your documents. Currently, citations must be enabled on all or none of the documents within a request.
* Note that only text citations are currently supported and image citations are not yet possible.
2
Documents get processed

* Document contents are “chunked” in order to define the minimum granularity of possible citations. For example, sentence chunking would allow Claude to cite a single sentence or chain together multiple consecutive sentences to cite a paragraph (or longer)!

For PDFs: Text is extracted as described in PDF Support and content is chunked into sentences. Citing images from PDFs is not currently supported.
For plain text documents: Content is chunked into sentences that can be cited from.
For custom content documents: Your provided content blocks are used as-is and no further chunking is done.
3
Claude provides cited response

* Responses may now include multiple text blocks where each text block can contain a claim that Claude is making and a list of citations that support the claim.
* Citations reference specific locations in source documents. The format of these citations are dependent on the type of document being cited from.

For PDFs: citations will include the page number range (1-indexed).
For plain text documents: Citations will include the character index range (0-indexed).
For custom content documents: Citations will include the content block index range (0-indexed) corresponding to the original content list provided.
* Document indices are provided to indicate the reference source and are 0-indexed according to the list of all documents in your original request.

Automatic chunking vs custom content

By default, plain text and PDF documents are automatically chunked into sentences. If you need more control over citation granularity (e.g., for bullet points or transcripts), use custom content documents instead. See Document Types for more details.

For example, if you want Claude to be able to cite specific sentences from your RAG chunks, you should put each RAG chunk into a plain text document. Otherwise, if you do not want any further chunking to be done, or if you want to customize any additional chunking, you can put RAG chunks into custom content document(s).

### ​Citable vs non-citable content

* Text found within a document’s source content can be cited from.
* title and context are optional fields that will be passed to the model but not used towards cited content.
* title is limited in length so you may find the context field to be useful in storing any document metadata as text or stringified json.

### ​Citation indices

* Document indices are 0-indexed from the list of all document content blocks in the request (spanning across all messages).
* Character indices are 0-indexed with exclusive end indices.
* Page numbers are 1-indexed with exclusive end page numbers.
* Content block indices are 0-indexed with exclusive end indices from the content list provided in the custom content document.

### ​Token costs

* Enabling citations incurs a slight increase in input tokens due to system prompt additions and document chunking.
* However, the citations feature is very efficient with output tokens. Under the hood, the model is outputting citations in a standardized format that are then parsed into cited text and document location indices. The cited_text field is provided for convenience and does not count towards output tokens.
* When passed back in subsequent conversation turns, cited_text is also not counted towards input tokens.

### ​Feature compatibility

Citations works in conjunction with other API features including prompt caching, token counting and batch processing.

## ​Document Types

### ​Choosing a document type

We support three document types for citations:
TypeBest forChunkingCitation formatPlain textSimple text documents, proseSentenceCharacter indices (0-indexed)PDFPDF files with text contentSentencePage numbers (1-indexed)Custom contentLists, transcripts, special formatting, more granular citationsNo additional chunkingBlock indices (0-indexed)
### ​Plain text documents

Plain text documents are automatically chunked into sentences:

```
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": "Plain text content..."
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

Example plain text citation

```
{
    "type": "char_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_char_index": 0,    # 0-indexed
    "end_char_index": 50      # exclusive
}
```

### ​PDF documents

PDF documents are provided as base64-encoded data. PDF text is extracted and chunked into sentences. As image citations are not yet supported, PDFs that are scans of documents and do not contain extractable text will not be citable.

```
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": base64_encoded_pdf_data
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

Example PDF citation

```
{
    "type": "page_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,     
    "document_title": "Document Title", 
    "start_page_number": 1,  # 1-indexed
    "end_page_number": 2     # exclusive
}
```

### ​Custom content documents

Custom content documents give you control over citation granularity. No additional chunking is done and chunks are provided to the model according to the content blocks provided.

```
{
    "type": "document",
    "source": {
        "type": "content",
        "content": [
            {"type": "text", "text": "First chunk"},
            {"type": "text", "text": "Second chunk"}
        ]
    },
    "title": "Document Title", # optional
    "context": "Context about the document that will not be cited from", # optional
    "citations": {"enabled": True}
}
```

Example citation

```
{
    "type": "content_block_location",
    "cited_text": "The exact text being cited", # not counted towards output tokens
    "document_index": 0,
    "document_title": "Document Title",
    "start_block_index": 0,   # 0-indexed
    "end_block_index": 1      # exclusive
}
```

## ​Response Structure

When citations are enabled, responses include multiple text blocks with citations:

```
{
    "content": [
        {
            "type": "text",
            "text": "According to the document, "
        },
        {
            "type": "text",
            "text": "the grass is green",
            "citations": [{
                "type": "char_location",
                "cited_text": "The grass is green.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 0,
                "end_char_index": 20
            }]
        },
        {
            "type": "text",
            "text": " and "
        },
        {
            "type": "text",
            "text": "the sky is blue",
            "citations": [{
                "type": "char_location",
                "cited_text": "The sky is blue.",
                "document_index": 0,
                "document_title": "Example Document",
                "start_char_index": 20,
                "end_char_index": 36
            }]
        }
    ]
}
```

### ​Streaming Support

For streaming responses, we’ve added a citations_delta type that contains a single citation to be added to the citations list on the current text content block.

Example streaming events

```
event: message_start
data: {"type": "message_start", ...}

event: content_block_start
data: {"type": "content_block_start", "index": 0, ...}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, 
       "delta": {"type": "text_delta", "text": "According to..."}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0,
       "delta": {"type": "citations_delta", 
                 "citation": {
                     "type": "char_location",
                     "cited_text": "...",
                     "document_index": 0,
                     ...
                 }}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: message_stop
data: {"type": "message_stop"}
```

Was this page helpful?
YesNo[PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)[Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How citations work
* Citable vs non-citable content
* Citation indices
* Token costs
* Feature compatibility
* Document Types
* Choosing a document type
* Plain text documents
* PDF documents
* Custom content documents
* Response Structure
* Streaming Support


---

## Computer use (beta)

Source: https://docs.anthropic.com/en/docs/agents-and-tools/computer-use

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationAgents and toolsComputer use (beta)[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Agents and tools
# Computer use (beta)

Claude 3.7 Sonnet and Claude 3.5 Sonnet (new) are capable of interacting with tools that can manipulate a computer desktop environment. Claude 3.7 Sonnet introduces additional tools and allows you to enable thinking, giving you more insight into the model’s reasoning process.

Computer use is a beta feature. Please be aware that computer use poses unique risks that are distinct from standard API features or chat interfaces. These risks are heightened when using computer use to interact with the internet. To minimize risks, consider taking precautions such as:

1. Use a dedicated virtual machine or container with minimal privileges to prevent direct system attacks or accidents.
2. Avoid giving the model access to sensitive data, such as account login information, to prevent information theft.
3. Limit internet access to an allowlist of domains to reduce exposure to malicious content.
4. Ask a human to confirm decisions that may result in meaningful real-world consequences as well as any tasks requiring affirmative consent, such as accepting cookies, executing financial transactions, or agreeing to terms of service.

In some circumstances, Claude will follow commands found in content even if it conflicts with the user’s instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. We suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

We’ve trained the model to resist these prompt injections and have added an extra layer of defense. If you use our computer use tools, we’ll automatically run classifiers on your prompts to flag potential instances of prompt injections. When these classifiers identify potential prompt injections in screenshots, they will automatically steer the model to ask for user confirmation before proceeding with the next action. We recognize that this extra protection won’t be ideal for every use case (for example, use cases without a human in the loop), so if you’d like to opt out and turn it off, please contact us.

We still suggest taking precautions to isolate Claude from sensitive data and actions to avoid risks related to prompt injection.

Finally, please inform end users of relevant risks and obtain their consent prior to enabling computer use in your own products.
[Computer use reference implementationGet started quickly with our computer use reference implementation that includes a web interface, Docker container, example tool implementations, and an agent loop.Note: The implementation has been updated to include new tools for Claude 3.7 Sonnet. Be sure to pull the latest version of the repo to access these new features.](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
Please use this form to provide
feedback on the quality of the model responses, the API itself, or the quality
of the documentation - we cannot wait to hear from you!

Here’s an example of how to provide computer use tools to Claude using the Messages API:

## ​How computer use works

1. Provide Claude with computer use tools and a user prompt

* Add Anthropic-defined computer use tools to your API request. - Include a
user prompt that might require these tools, e.g., “Save a picture of a cat
to my desktop.”

2. Claude decides to use a tool

* Claude loads the stored computer use tool definitions and assesses if any
tools can help with the user’s query. - If yes, Claude constructs a properly
formatted tool use request. - The API response has a stop_reason of
tool_use, signaling Claude’s intent.

3. Extract tool input, evaluate the tool on a computer, and return results

* On your end, extract the tool name and input from Claude’s request. - Use
the tool on a container or Virtual Machine. - Continue the conversation with
a new user message containing a tool_result content block.

4. Claude continues calling computer use tools until it's completed the task

* Claude analyzes the tool results to determine if more tool use is needed
or the task has been completed. - If Claude decides it needs another tool,
it responds with another tool_use stop_reason and you should return to
step 3. - Otherwise, it crafts a text response to the user.

We refer to the repetition of steps 3 and 4 without user input as the “agent loop” - i.e., Claude responding with a tool use request and your application responding to Claude with the results of evaluating that request.

### ​The computing environment

Computer use requires a sandboxed computing environment where Claude can safely interact with applications and the web. This environment includes:

1. Virtual display: A virtual X11 display server (using Xvfb) that renders the desktop interface Claude will see through screenshots and control with mouse/keyboard actions.
2. Desktop environment: A lightweight UI with window manager (Mutter) and panel (Tint2) running on Linux, which provides a consistent graphical interface for Claude to interact with.
3. Applications: Pre-installed Linux applications like Firefox, LibreOffice, text editors, and file managers that Claude can use to complete tasks.
4. Tool implementations: Integration code that translates Claude’s abstract tool requests (like “move mouse” or “take screenshot”) into actual operations in the virtual environment.
5. Agent loop: A program that handles communication between Claude and the environment, sending Claude’s actions to the environment and returning the results (screenshots, command outputs) back to Claude.

When you use computer use, Claude doesn’t directly connect to this environment. Instead, your application:

1. Receives Claude’s tool use requests
2. Translates them into actions in your computing environment
3. Captures the results (screenshots, command outputs, etc.)
4. Returns these results to Claude

For security and isolation, the reference implementation runs all of this inside a Docker container with appropriate port mappings for viewing and interacting with the environment.

## ​How to implement computer use

### ​Start with our reference implementation

We have built a reference implementation that includes everything you need to get started quickly with computer use:

* A containerized environment suitable for computer use with Claude
* Implementations of the computer use tools
* An agent loop that interacts with the Anthropic API and executes the computer use tools
* A web interface to interact with the container, agent loop, and tools.

### ​Understanding the multi-agent loop

The core of computer use is the “agent loop” - a cycle where Claude requests tool actions, your application executes them, and returns results to Claude. Here’s a simplified example:

```
async def sampling_loop(
    *,
    model: str,
    messages: list[dict],
    api_key: str,
    max_tokens: int = 4096,
    tool_version: str,
    thinking_budget: int | None = None,
    max_iterations: int = 10,  # Add iteration limit to prevent infinite loops
):
    """
    A simple agent loop for Claude computer use interactions.

    This function handles the back-and-forth between:
    1. Sending user messages to Claude
    2. Claude requesting to use tools
    3. Your app executing those tools
    4. Sending tool results back to Claude
    """
    # Set up tools and API parameters
    client = Anthropic(api_key=api_key)
    beta_flag = "computer-use-2025-01-24" if "20250124" in tool_version else "computer-use-2024-10-22"

    # Configure tools - you should already have these initialized elsewhere
    tools = [
        {"type": f"computer_{tool_version}", "name": "computer", "display_width_px": 1024, "display_height_px": 768},
        {"type": f"text_editor_{tool_version}", "name": "str_replace_editor"},
        {"type": f"bash_{tool_version}", "name": "bash"}
    ]

    # Main agent loop (with iteration limit to prevent runaway API costs)
    iterations = 0
    while True and iterations < max_iterations:
        iterations += 1
        # Set up optional thinking parameter (for Claude 3.7 Sonnet)
        thinking = None
        if thinking_budget:
            thinking = {"type": "enabled", "budget_tokens": thinking_budget}

        # Call the Claude API
        response = client.beta.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=messages,
            tools=tools,
            betas=[beta_flag],
            thinking=thinking
        )

        # Add Claude's response to the conversation history
        response_content = response.content
        messages.append({"role": "assistant", "content": response_content})

        # Check if Claude used any tools
        tool_results = []
        for block in response_content:
            if block.type == "tool_use":
                # In a real app, you would execute the tool here
                # For example: result = run_tool(block.name, block.input)
                result = {"result": "Tool executed successfully"}

                # Format the result for Claude
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result
                })

        # If no tools were used, Claude is done - return the final messages
        if not tool_results:
            return messages

        # Add tool results to messages for the next iteration with Claude
        messages.append({"role": "user", "content": tool_results})
```

The loop continues until either Claude responds without requesting any tools (task completion) or the maximum iteration limit is reached. This safeguard prevents potential infinite loops that could result in unexpected API costs.

For each version of the tools, you must use the corresponding beta flag in
your API request:

Claude 3.7 Sonnet beta flag

When using tools with 20250124 in their type (Claude 3.7 Sonnet tools),
include this beta flag: "betas": ["computer-use-2025-01-24"] Note:
The Bash (bash_20250124) and Text Editor (text_editor_20250124) tools
are generally available for Claude 3.5 Sonnet (new) as well and can be
used without the computer use beta header.

Claude 3.5 Sonnet (new) beta flag

When using tools with 20241022 in their type (Claude 3.5 Sonnet tools),
include this beta flag: "betas": ["computer-use-2024-10-22"]

We recommend trying the reference implementation out before reading the rest of this documentation.

### ​Optimize model performance with prompting

Here are some tips on how to get the best quality outputs:

1. Specify simple, well-defined tasks and provide explicit instructions for each step.
2. Claude sometimes assumes outcomes of its actions without explicitly checking their results. To prevent this you can prompt Claude with After each step, take a screenshot and carefully evaluate if you have achieved the right outcome. Explicitly show your thinking: "I have evaluated step X..." If not correct, try again. Only when you confirm a step was executed correctly should you move on to the next one.
3. Some UI elements (like dropdowns and scrollbars) might be tricky for Claude to manipulate using mouse movements. If you experience this, try prompting the model to use keyboard shortcuts.
4. For repeatable tasks or UI interactions, include example screenshots and tool calls of successful outcomes in your prompt.
5. If you need the model to log in, provide it with the username and password in your prompt inside xml tags like <robot_credentials>. Using computer use within applications that require login increases the risk of bad outcomes as a result of prompt injection. Please review our guide on mitigating prompt injections before providing the model with login credentials.

If you repeatedly encounter a clear set of issues or know in advance the tasks
Claude will need to complete, use the system prompt to provide Claude with
explicit tips or instructions on how to do the tasks successfully.

#### ​System prompts

When one of the Anthropic-defined tools is requested via the Anthropic API, a computer use-specific system prompt is generated. It’s similar to the tool use system prompt but starts with:

You have access to a set of functions you can use to answer the user’s question. This includes access to a sandboxed computing environment. You do NOT currently have the ability to inspect files or interact with external resources, except by invoking the below functions.

As with regular tool use, the user-provided system_prompt field is still respected and used in the construction of the combined system prompt.

### ​Understand Anthropic-defined tools
As a beta, these tool definitions are subject to change.
We have provided a set of tools that enable Claude to effectively use computers. When specifying an Anthropic-defined tool, description and tool_schema fields are not necessary or allowed.

Anthropic-defined tools are user executed

Anthropic-defined tools are defined by Anthropic but you must explicitly evaluate the results of the tool and return the tool_results to Claude. As with any tool, the model does not automatically execute the tool.

We provide a set of Anthropic-defined tools, with each tool having versions optimized for both Claude 3.5 Sonnet (new) and Claude 3.7 Sonnet:

Claude 3.7 Sonnet tools

The following enhanced tools can be used with Claude 3.7 Sonnet:

* { "type": "computer_20250124", "name": "computer" } - Includes new actions for more precise control
* { "type": "text_editor_20250124", "name": "str_replace_editor" } - Same capabilities as 20241022 version
* { "type": "bash_20250124", "name": "bash" } - Same capabilities as 20241022 version

When using Claude 3.7 Sonnet, you can also enable the extended thinking capability to understand the model’s reasoning process.

Claude 3.5 Sonnet (new) tools

The following tools can be used with Claude 3.5 Sonnet (new):

* { "type": "computer_20241022", "name": "computer" }
* { "type": "text_editor_20241022", "name": "str_replace_editor" }
* { "type": "bash_20241022", "name": "bash" }

The type field identifies the tool and its parameters for validation purposes, the name field is the tool name exposed to the model.

If you want to prompt the model to use one of these tools, you can explicitly refer the tool by the name field. The name field must be unique within the tool list; you cannot define a tool with the same name as an Anthropic-defined tool in the same API call.

We do not recommend defining tools with the names of Anthropic-defined tools.
While you can still redefine tools with these names (as long as the tool name
is unique in your tools block), doing so may result in degraded model
performance.

Computer tool

We do not recommend sending screenshots in resolutions above XGA/WXGA to avoid issues related to image resizing.
Relying on the image resizing behavior in the API will result in lower model accuracy and slower performance than directly implementing scaling yourself.

The reference repository demonstrates how to scale from higher resolutions to a suggested resolution.

#### Types

* computer_20250124 - Enhanced computer tool with additional actions available in Claude 3.7 Sonnet
* computer_20241022 - Original computer tool used with Claude 3.5 Sonnet (new)

#### Parameters

* display_width_px: Required The width of the display being controlled by the model in pixels.
* display_height_px: Required The height of the display being controlled by the model in pixels.
* display_number: Optional The display number to control (only relevant for X11 environments). If specified, the tool will be provided a display number in the tool definition.

#### Tool description

We are providing our tool description for reference only. You should not specify this in your Anthropic-defined tool call.

```
Use a mouse and keyboard to interact with a computer, and take screenshots.
* This is an interface to a desktop GUI. You do not have access to a terminal or applications menu. You must click on desktop icons to start applications.
* Some applications may take time to start or process actions, so you may need to wait and take successive screenshots to see the results of your actions. E.g. if you click on Firefox and a window doesn't open, try taking another screenshot.
* The screen's resolution is {{ display_width_px }}x{{ display_height_px }}.
* The display number is {{ display_number }}
* Whenever you intend to move the cursor to click on an element like an icon, you should consult a screenshot to determine the coordinates of the element before moving the cursor.
* If you tried clicking on a program or link but it failed to load, even after waiting, try adjusting your cursor position so that the tip of the cursor visually falls on the element that you want to click.
* Make sure to click any buttons, links, icons, etc with the cursor tip in the center of the element. Don't click boxes on their edges unless asked.
```

#### Tool input schema

We are providing our input schema for reference only. For the enhanced computer_20250124 tool available with Claude 3.7 Sonnet. Here is the full input schema:

```
{
    "properties": {
        "action": {
            "description": "The action to perform. The available actions are:\n"
            "* `key`: Press a key or key-combination on the keyboard.\n"
            "  - This supports xdotool's `key` syntax.\n"
            '  - Examples: "a", "Return", "alt+Tab", "ctrl+s", "Up", "KP_0" (for the numpad 0 key).\n'
            "* `hold_key`: Hold down a key or multiple keys for a specified duration (in seconds). Supports the same syntax as `key`.\n"
            "* `type`: Type a string of text on the keyboard.\n"
            "* `cursor_position`: Get the current (x, y) pixel coordinate of the cursor on the screen.\n"
            "* `mouse_move`: Move the cursor to a specified (x, y) pixel coordinate on the screen.\n"
            "* `left_mouse_down`: Press the left mouse button.\n"
            "* `left_mouse_up`: Release the left mouse button.\n"
            "* `left_click`: Click the left mouse button at the specified (x, y) pixel coordinate on the screen. You can also include a key combination to hold down while clicking using the `text` parameter.\n"
            "* `left_click_drag`: Click and drag the cursor from `start_coordinate` to a specified (x, y) pixel coordinate on the screen.\n"
            "* `right_click`: Click the right mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `middle_click`: Click the middle mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `double_click`: Double-click the left mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `triple_click`: Triple-click the left mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `scroll`: Scroll the screen in a specified direction by a specified amount of clicks of the scroll wheel, at the specified (x, y) pixel coordinate. DO NOT use PageUp/PageDown to scroll.\n"
            "* `wait`: Wait for a specified duration (in seconds).\n"
            "* `screenshot`: Take a screenshot of the screen.",
            "enum": [
                "key",
                "hold_key",
                "type",
                "cursor_position",
                "mouse_move",
                "left_mouse_down",
                "left_mouse_up",
                "left_click",
                "left_click_drag",
                "right_click",
                "middle_click",
                "double_click",
                "triple_click",
                "scroll",
                "wait",
                "screenshot",
            ],
            "type": "string",
        },
        "coordinate": {
            "description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to move the mouse to. Required only by `action=mouse_move` and `action=left_click_drag`.",
            "type": "array",
        },
        "duration": {
            "description": "The duration to hold the key down for. Required only by `action=hold_key` and `action=wait`.",
            "type": "integer",
        },
        "scroll_amount": {
            "description": "The number of 'clicks' to scroll. Required only by `action=scroll`.",
            "type": "integer",
        },
        "scroll_direction": {
            "description": "The direction to scroll the screen. Required only by `action=scroll`.",
            "enum": ["up", "down", "left", "right"],
            "type": "string",
        },
        "start_coordinate": {
            "description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to start the drag from. Required only by `action=left_click_drag`.",
            "type": "array",
        },
        "text": {
            "description": "Required only by `action=type`, `action=key`, and `action=hold_key`. Can also be used by click or scroll actions to hold down keys while clicking or scrolling.",
            "type": "string",
        },
    },
    "required": ["action"],
    "type": "object",
}
```

For the original computer_20241022 tool used with Claude 3.5 Sonnet (new):

```
{
    "properties": {
        "action": {
            "description": """The action to perform. The available actions are:
                * `key`: Press a key or key-combination on the keyboard.
                  - This supports xdotool's `key` syntax.
                  - Examples: "a", "Return", "alt+Tab", "ctrl+s", "Up", "KP_0" (for the numpad 0 key).
                * `type`: Type a string of text on the keyboard.
                * `cursor_position`: Get the current (x, y) pixel coordinate of the cursor on the screen.
                * `mouse_move`: Move the cursor to a specified (x, y) pixel coordinate on the screen.
                * `left_click`: Click the left mouse button.
                * `left_click_drag`: Click and drag the cursor to a specified (x, y) pixel coordinate on the screen.
                * `right_click`: Click the right mouse button.
                * `middle_click`: Click the middle mouse button.
                * `double_click`: Double-click the left mouse button.
                * `screenshot`: Take a screenshot of the screen.""",
            "enum": [
                "key",
                "type",
                "mouse_move",
                "left_click",
                "left_click_drag",
                "right_click",
                "middle_click",
                "double_click",
                "screenshot",
                "cursor_position",
            ],
            "type": "string",
        },
        "coordinate": {
            "description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to move the mouse to. Required only by `action=mouse_move` and `action=left_click_drag`.",
            "type": "array",
        },
        "text": {
            "description": "Required only by `action=type` and `action=key`.",
            "type": "string",
        },
    },
    "required": ["action"],
    "type": "object",
}
```

Text editor tool

#### Types

* text_editor_20250124 - Same capabilities as the 20241022 version, for use with Claude 3.7 Sonnet
* text_editor_20241022 - Original text editor tool used with Claude 3.5 Sonnet (new)

#### Tool description

We are providing our tool description for reference only. You should not specify this in your Anthropic-defined tool call.

```
Custom editing tool for viewing, creating and editing files
* State is persistent across command calls and discussions with the user
* If `path` is a file, `view` displays the result of applying `cat -n`. If `path` is a directory, `view` lists non-hidden files and directories up to 2 levels deep
* The `create` command cannot be used if the specified `path` already exists as a file
* If a `command` generates a long output, it will be truncated and marked with `<response clipped>`
* The `undo_edit` command will revert the last edit made to the file at `path`

Notes for using the `str_replace` command:
* The `old_str` parameter should match EXACTLY one or more consecutive lines from the original file. Be mindful of whitespaces!
* If the `old_str` parameter is not unique in the file, the replacement will not be performed. Make sure to include enough context in `old_str` to make it unique
* The `new_str` parameter should contain the edited lines that should replace the `old_str`
```

#### Tool input schema

We are providing our input schema for reference only. You should not specify this in your Anthropic-defined tool call.

```
{
    "properties": {
        "command": {
            "description": "The commands to run. Allowed options are: `view`, `create`, `str_replace`, `insert`, `undo_edit`.",
            "enum": ["view", "create", "str_replace", "insert", "undo_edit"],
            "type": "string",
        },
        "file_text": {
            "description": "Required parameter of `create` command, with the content of the file to be created.",
            "type": "string",
        },
        "insert_line": {
            "description": "Required parameter of `insert` command. The `new_str` will be inserted AFTER the line `insert_line` of `path`.",
            "type": "integer",
        },
        "new_str": {
            "description": "Optional parameter of `str_replace` command containing the new string (if not given, no string will be added). Required parameter of `insert` command containing the string to insert.",
            "type": "string",
        },
        "old_str": {
            "description": "Required parameter of `str_replace` command containing the string in `path` to replace.",
            "type": "string",
        },
        "path": {
            "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
            "type": "string",
        },
        "view_range": {
            "description": "Optional parameter of `view` command when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
            "items": {"type": "integer"},
            "type": "array",
        },
    },
    "required": ["command", "path"],
    "type": "object",
}
```

Bash tool

#### Types

* bash_20250124 - Same capabilities as the 20241022 version, for use with Claude 3.7 Sonnet
* bash_20241022 - Original bash tool used with Claude 3.5 Sonnet (new)

#### Tool description

We are providing our tool description for reference only. You should not specify this in your Anthropic-defined tool call.

```
Run commands in a bash shell
* When invoking this tool, the contents of the "command" parameter does NOT need to be XML-escaped.
* You have access to a mirror of common linux and python packages via apt and pip.
* State is persistent across command calls and discussions with the user.
* To inspect a particular line range of a file, e.g. lines 10-25, try 'sed -n 10,25p /path/to/the/file'.
* Please avoid commands that may produce a very large amount of output.
* Please run long lived commands in the background, e.g. 'sleep 10 &' or start a server in the background.
```

#### Tool input schema

We are providing our input schema for reference only. You should not specify this in your Anthropic-defined tool call.

```
{
    "properties": {
        "command": {
            "description": "The bash command to run. Required unless the tool is being restarted.",
            "type": "string",
        },
        "restart": {
            "description": "Specifying true will restart this tool. Otherwise, leave this unspecified.",
            "type": "boolean",
        },
    }
}
```

### ​Enable thinking capability in Claude 3.7 Sonnet

Claude 3.7 Sonnet introduces a new “thinking” capability that allows you to see the model’s reasoning process as it works through complex tasks. This feature helps you understand how Claude is approaching a problem and can be particularly valuable for debugging or educational purposes.

To enable thinking, add a thinking parameter to your API request:

```
"thinking": {
  "type": "enabled",
  "budget_tokens": 1024
}
```

The budget_tokens parameter specifies how many tokens Claude can use for thinking. This is subtracted from your overall max_tokens budget.

When thinking is enabled, Claude will return its reasoning process as part of the response, which can help you:

1. Understand the model’s decision-making process
2. Identify potential issues or misconceptions
3. Learn from Claude’s approach to problem-solving
4. Get more visibility into complex multi-step operations

Here’s an example of what thinking output might look like:

```
[Thinking]
I need to save a picture of a cat to the desktop. Let me break this down into steps:

1. First, I'll take a screenshot to see what's on the desktop
2. Then I'll look for a web browser to search for cat images
3. After finding a suitable image, I'll need to save it to the desktop

Let me start by taking a screenshot to see what's available...
```

### ​Combine computer use with other tools

You can combine regular tool use with the Anthropic-defined tools for computer use.

### ​Build a custom computer use environment

The reference implementation is meant to help you get started with computer use. It includes all of the components needed have Claude use a computer. However, you can build your own environment for computer use to suit your needs. You’ll need:

* A virtualized or containerized environment suitable for computer use with Claude
* An implementation of at least one of the Anthropic-defined computer use tools
* An agent loop that interacts with the Anthropic API and executes the tool_use results using your tool implementations
* An API or UI that allows user input to start the agent loop

## ​Understand computer use limitations

The computer use functionality is in beta. While Claude’s capabilities are cutting edge, developers should be aware of its limitations:

1. Latency: the current computer use latency for human-AI interactions may be too slow compared to regular human-directed computer actions. We recommend focusing on use cases where speed isn’t critical (e.g., background information gathering, automated software testing) in trusted environments.
2. Computer vision accuracy and reliability: Claude may make mistakes or hallucinate when outputting specific coordinates while generating actions. Claude 3.7 Sonnet introduces the thinking capability that can help you understand the model’s reasoning and identify potential issues.
3. Tool selection accuracy and reliability: Claude may make mistakes or hallucinate when selecting tools while generating actions or take unexpected actions to solve problems. Additionally, reliability may be lower when interacting with niche applications or multiple applications at once. We recommend that users prompt the model carefully when requesting complex tasks.
4. Scrolling reliability: While Claude 3.5 Sonnet (new) had limitations with scrolling, Claude 3.7 Sonnet introduces dedicated scroll actions with direction control that improves reliability. The model can now explicitly scroll in any direction (up/down/left/right) by a specified amount.
5. Spreadsheet interaction: Mouse clicks for spreadsheet interaction have improved in Claude 3.7 Sonnet with the addition of more precise mouse control actions like left_mouse_down, left_mouse_up, and new modifier key support. Cell selection can be more reliable by using these fine-grained controls and combining modifier keys with clicks.
6. Account creation and content generation on social and communications platforms: While Claude will visit websites, we are limiting its ability to create accounts or generate and share content or otherwise engage in human impersonation across social media websites and platforms. We may update this capability in the future.
7. Vulnerabilities: Vulnerabilities like jailbreaking or prompt injection may persist across frontier AI systems, including the beta computer use API. In some circumstances, Claude will follow commands found in content, sometimes even in conflict with the user’s instructions. For example, Claude instructions on webpages or contained in images may override instructions or cause Claude to make mistakes. We recommend:
a. Limiting computer use to trusted environments such as virtual machines or containers with minimal privileges
b. Avoiding giving computer use access to sensitive accounts or data without strict oversight
c. Informing end users of relevant risks and obtaining their consent before enabling or requesting permissions necessary for computer use features in your applications
8. Inappropriate or illegal actions: Per Anthropic’s terms of service, you must not employ computer use to violate any laws or our Acceptable Use Policy.

Always carefully review and verify Claude’s computer use actions and logs. Do not use Claude for tasks requiring perfect precision or sensitive user information without human oversight.

## ​Pricing

See the tool use pricing
documentation for a detailed explanation of how Claude Tool Use API requests
are priced.

As a subset of tool use requests, computer use requests are priced the same as any other Claude API request.

We also automatically include a special system prompt for the model, which enables computer use.
ModelTool choiceSystem prompt token countClaude 3.5 Sonnet (new)`auto``any`,`tool`466 tokens499 tokensClaude 3.7 Sonnet`auto``any`,`tool`466 tokens499 tokens
In addition to the base tokens, the following additional input tokens are needed for the Anthropic-defined tools:
ToolAdditional input tokens`computer_20241022`(Claude 3.5 Sonnet)683 tokens`computer_20250124`(Claude 3.7 Sonnet)735 tokens`text_editor_20241022`(Claude 3.5 Sonnet)700 tokens`text_editor_20250124`(Claude 3.7 Sonnet)700 tokens`bash_20241022`(Claude 3.5 Sonnet)245 tokens`bash_20250124`(Claude 3.7 Sonnet)245 tokens
If you enable thinking with Claude 3.7 Sonnet, the tokens used for thinking will be counted against your max_tokens budget based on the budget_tokens you specify in the thinking parameter.

Was this page helpful?
YesNo[Troubleshooting](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/troubleshooting)[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How computer use works
* The computing environment
* How to implement computer use
* Start with our reference implementation
* Understanding the multi-agent loop
* Optimize model performance with prompting
* System prompts
* Understand Anthropic-defined tools
* Enable thinking capability in Claude 3.7 Sonnet
* Combine computer use with other tools
* Build a custom computer use environment
* Understand computer use limitations
* Pricing


---

## Context windows

Source: https://docs.anthropic.com/en/docs/build-with-claude/context-windows

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeContext windows[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Context windows

## ​Understanding the context window

The “context window” refers to the entirety of the amount of text a language model can look back on and reference when generating new text plus the new text it generates. This is different from the large corpus of data the language model was trained on, and instead represents a “working memory” for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model’s ability to handle longer prompts or maintain coherence over extended conversations.

The diagram below illustrates the standard context window behavior for API requests1:



1For chat interfaces, such as for claude.ai, context windows can also be set up on a rolling “first in, first out” system.

* Progressive token accumulation: As the conversation advances through turns, each user message and assistant response accumulates within the context window. Previous turns are preserved completely.
* Linear growth pattern: The context usage grows linearly with each turn, with previous turns preserved completely.
* 200K token capacity: The total available context window (200,000 tokens) represents the maximum capacity for storing conversation history and generating new output from Claude.
* Input-output flow: Each turn consists of:

Input phase: Contains all previous conversation history plus the current user message
Output phase: Generates a text response that becomes part of a future input

## ​The context window with extended thinking

When using extended thinking, all input and output tokens, including the tokens used for thinking, count toward the context window limit, with a few nuances in multi-turn situations.

The thinking budget tokens are a subset of your max_tokens parameter, are billed as output tokens, and count towards rate limits.

However, previous thinking blocks are automatically stripped from the context window calculation by the Anthropic API and are not part of the conversation history that the model “sees” for subsequent turns, preserving token capacity for actual conversation content.

The diagram below demonstrates the specialized token management when extended thinking is enabled:



* Stripping extended thinking: Extended thinking blocks (shown in dark gray) are generated during each turn’s output phase, but are not carried forward as input tokens for subsequent turns. You do not need to strip the thinking blocks yourself. The Anthropic API automatically does this for you if you pass them back.
* Technical implementation details:

The API automatically excludes thinking blocks from previous turns when you pass them back as part of the conversation history.
Extended thinking tokens are billed as output tokens only once, during their generation.
The effective context window calculation becomes: context_window = (input_tokens - previous_thinking_tokens) + current_turn_tokens.
Thinking tokens include both thinking blocks and redacted_thinking blocks.

This architecture is token efficient and allows for extensive reasoning without token waste, as thinking blocks can be substantial in length.

You can read more about the context window and extended thinking in our extended thinking guide.

## ​The context window with extended thinking and tool use

The diagram below illustrates the context window token management when combining extended thinking with tool use:


1
First turn architecture

* Input components: Tools configuration and user message
* Output components: Extended thinking + text response + tool use request
* Token calculation: All input and output components count toward the context window, and all output components are billed as output tokens.
2
Tool result handling (turn 2)

* Input components: Every block in the first turn as well as the tool_result. The extended thinking block must be returned with the corresponding tool results. This is the only case wherein you have to return thinking blocks.
* Output components: After tool results have been passed back to Claude, Claude will respond with only text (no additional extended thinking until the next user message).
* Token calculation: All input and output components count toward the context window, and all output components are billed as output tokens.
3
Third Step

* Input components: All inputs and the output from the previous turn is carried forward with the exception of the thinking block, which can be dropped now that Claude has completed the entire tool use cycle. The API will automatically strip the thinking block for you if you pass it back, or you can feel free to strip it yourself at this stage. This is also where you would add the next User turn.
* Output components: Since there is a new User turn outside of the tool use cycle, Claude will generate a new extended thinking block and continue from there.
* Token calculation: Previous thinking tokens are automatically stripped from context window calculations. All other previous blocks still count as part of the token window, and the thinking block in the current Assistant turn counts as part of the context window.

* Considerations for tool use with extended thinking:

When posting tool results, the entire unmodified thinking block that accompanies that specific tool request (including signature/redacted portions) must be included.
The system uses cryptographic signatures to verify thinking block authenticity. Failing to preserve thinking blocks during tool use can break Claude’s reasoning continuity. Thus, if you modify thinking blocks, the API will return an error.

There is no interleaving of extended thinking and tool calls - you won’t see extended thinking, then tool calls, then more extended thinking, without a non-tool_result user turn in between. Additionally, tool use within the extended thinking block itself is not currently supported, although Claude may reason about what tools it should use and how to call them within the thinking block.

You can read more about tool use with extended thinking in our extended thinking guide

### ​Context window management with newer Claude models

In newer Claude models (starting with Claude 3.7 Sonnet), if the sum of prompt tokens and output tokens exceeds the model’s context window, the system will return a validation error rather than silently truncating the context. This change provides more predictable behavior but requires more careful token management.

To plan your token usage and ensure you stay within context window limits, you can use the token counting API to estimate how many tokens your messages will use before sending them to Claude.

See our model comparison table for a list of context window sizes by model.

# ​Next steps
[Model comparison tableSee our model comparison table for a list of context window sizes and input / output token pricing by model.](https://docs.anthropic.com/en/docs/models-overview#model-comparison)[Extended thinking overviewLearn more about how extended thinking works and how to implement it alongside other features such as tool use and prompt caching.](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
Was this page helpful?
YesNo[Develop test cases](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)[Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Understanding the context window
* The context window with extended thinking
* The context window with extended thinking and tool use
* Context window management with newer Claude models
* Next steps


---

## Create strong empirical evaluations

Source: https://docs.anthropic.com/en/docs/build-with-claude/develop-tests

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeCreate strong empirical evaluations[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Create strong empirical evaluations

After defining your success criteria, the next step is designing evaluations to measure LLM performance against those criteria. This is a vital part of the prompt engineering cycle.



This guide focuses on how to develop your test cases.

## ​Building evals and test cases

### ​Eval design principles

1. Be task-specific: Design evals that mirror your real-world task distribution. Don’t forget to factor in edge cases!
Example edge cases
Irrelevant or nonexistent input data
Overly long input data or user input
[Chat use cases] Poor, harmful, or irrelevant user input
Ambiguous test cases where even humans would find it hard to reach an assessment consensus
2. Automate when possible: Structure questions to allow for automated grading (e.g., multiple-choice, string match, code-graded, LLM-graded).
3. Prioritize volume over quality: More questions with slightly lower signal automated grading is better than fewer questions with high-quality human hand-graded evals.

### ​Example evals

Task fidelity (sentiment analysis) - exact match evaluation

What it measures: Exact match evals measure whether the model’s output exactly matches a predefined correct answer. It’s a simple, unambiguous metric that’s perfect for tasks with clear-cut, categorical answers like sentiment analysis (positive, negative, neutral).

Example eval test cases: 1000 tweets with human-labeled sentiments.

```
import anthropic

tweets = [
    {"text": "This movie was a total waste of time. 👎", "sentiment": "negative"},
    {"text": "The new album is 🔥! Been on repeat all day.", "sentiment": "positive"},
    {"text": "I just love it when my flight gets delayed for 5 hours. #bestdayever", "sentiment": "negative"},  # Edge case: Sarcasm
    {"text": "The movie's plot was terrible, but the acting was phenomenal.", "sentiment": "mixed"},  # Edge case: Mixed sentiment
    # ... 996 more tweets
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=50,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_exact_match(model_output, correct_answer):
    return model_output.strip().lower() == correct_answer.lower()

outputs = [get_completion(f"Classify this as 'positive', 'negative', 'neutral', or 'mixed': {tweet['text']}") for tweet in tweets]
accuracy = sum(evaluate_exact_match(output, tweet['sentiment']) for output, tweet in zip(outputs, tweets)) / len(tweets)
print(f"Sentiment Analysis Accuracy: {accuracy * 100}%")
```

Consistency (FAQ bot) - cosine similarity evaluation

What it measures: Cosine similarity measures the similarity between two vectors (in this case, sentence embeddings of the model’s output using SBERT) by computing the cosine of the angle between them. Values closer to 1 indicate higher similarity. It’s ideal for evaluating consistency because similar questions should yield semantically similar answers, even if the wording varies.

Example eval test cases: 50 groups with a few paraphrased versions each.

```
from sentence_transformers import SentenceTransformer
import numpy as np
import anthropic

faq_variations = [
    {"questions": ["What's your return policy?", "How can I return an item?", "Wut's yur retrn polcy?"], "answer": "Our return policy allows..."},  # Edge case: Typos
    {"questions": ["I bought something last week, and it's not really what I expected, so I was wondering if maybe I could possibly return it?", "I read online that your policy is 30 days but that seems like it might be out of date because the website was updated six months ago, so I'm wondering what exactly is your current policy?"], "answer": "Our return policy allows..."},  # Edge case: Long, rambling question
    {"questions": ["I'm Jane's cousin, and she said you guys have great customer service. Can I return this?", "Reddit told me that contacting customer service this way was the fastest way to get an answer. I hope they're right! What is the return window for a jacket?"], "answer": "Our return policy allows..."},  # Edge case: Irrelevant info
    # ... 47 more FAQs
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=2048,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_cosine_similarity(outputs):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = [model.encode(output) for output in outputs]

    cosine_similarities = np.dot(embeddings, embeddings.T) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(embeddings, axis=1).T)
    return np.mean(cosine_similarities)

for faq in faq_variations:
    outputs = [get_completion(question) for question in faq["questions"]]
    similarity_score = evaluate_cosine_similarity(outputs)
    print(f"FAQ Consistency Score: {similarity_score * 100}%")
```

Relevance and coherence (summarization) - ROUGE-L evaluation

What it measures: ROUGE-L (Recall-Oriented Understudy for Gisting Evaluation - Longest Common Subsequence) evaluates the quality of generated summaries. It measures the length of the longest common subsequence between the candidate and reference summaries. High ROUGE-L scores indicate that the generated summary captures key information in a coherent order.

Example eval test cases: 200 articles with reference summaries.

```
from rouge import Rouge
import anthropic

articles = [
    {"text": "In a groundbreaking study, researchers at MIT...", "summary": "MIT scientists discover a new antibiotic..."},
    {"text": "Jane Doe, a local hero, made headlines last week for saving... In city hall news, the budget... Meteorologists predict...", "summary": "Community celebrates local hero Jane Doe while city grapples with budget issues."},  # Edge case: Multi-topic
    {"text": "You won't believe what this celebrity did! ... extensive charity work ...", "summary": "Celebrity's extensive charity work surprises fans"},  # Edge case: Misleading title
    # ... 197 more articles
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_rouge_l(model_output, true_summary):
    rouge = Rouge()
    scores = rouge.get_scores(model_output, true_summary)
    return scores[0]['rouge-l']['f']  # ROUGE-L F1 score

outputs = [get_completion(f"Summarize this article in 1-2 sentences:\n\n{article['text']}") for article in articles]
relevance_scores = [evaluate_rouge_l(output, article['summary']) for output, article in zip(outputs, articles)]
print(f"Average ROUGE-L F1 Score: {sum(relevance_scores) / len(relevance_scores)}")
```

Tone and style (customer service) - LLM-based Likert scale

What it measures: The LLM-based Likert scale is a psychometric scale that uses an LLM to judge subjective attitudes or perceptions. Here, it’s used to rate the tone of responses on a scale from 1 to 5. It’s ideal for evaluating nuanced aspects like empathy, professionalism, or patience that are difficult to quantify with traditional metrics.

Example eval test cases: 100 customer inquiries with target tone (empathetic, professional, concise).

```
import anthropic

inquiries = [
    {"text": "This is the third time you've messed up my order. I want a refund NOW!", "tone": "empathetic"},  # Edge case: Angry customer
    {"text": "I tried resetting my password but then my account got locked...", "tone": "patient"},  # Edge case: Complex issue
    {"text": "I can't believe how good your product is. It's ruined all others for me!", "tone": "professional"},  # Edge case: Compliment as complaint
    # ... 97 more inquiries
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=2048,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_likert(model_output, target_tone):
    tone_prompt = f"""Rate this customer service response on a scale of 1-5 for being {target_tone}:
    <response>{model_output}</response>
    1: Not at all {target_tone}
    5: Perfectly {target_tone}
    Output only the number."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output 
    response = client.messages.create(model="claude-3-opus-20240229", max_tokens=50, messages=[{"role": "user", "content": tone_prompt}])
    return int(response.content[0].text.strip())

outputs = [get_completion(f"Respond to this customer inquiry: {inquiry['text']}") for inquiry in inquiries]
tone_scores = [evaluate_likert(output, inquiry['tone']) for output, inquiry in zip(outputs, inquiries)]
print(f"Average Tone Score: {sum(tone_scores) / len(tone_scores)}")
```

Privacy preservation (medical chatbot) - LLM-based binary classification

What it measures: Binary classification determines if an input belongs to one of two classes. Here, it’s used to classify whether a response contains PHI or not. This method can understand context and identify subtle or implicit forms of PHI that rule-based systems might miss.

Example eval test cases: 500 simulated patient queries, some with PHI.

```
import anthropic

patient_queries = [
    {"query": "What are the side effects of Lisinopril?", "contains_phi": False},
    {"query": "Can you tell me why John Doe, DOB 5/12/1980, was prescribed Metformin?", "contains_phi": True},  # Edge case: Explicit PHI
    {"query": "If my friend Alice, who was born on July 4, 1985, had diabetes, what...", "contains_phi": True},  # Edge case: Hypothetical PHI
    {"query": "I'm worried about my son. He's been prescribed the same medication as his father last year.", "contains_phi": True},  # Edge case: Implicit PHI
    # ... 496 more queries
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_binary(model_output, query_contains_phi):
    if not query_contains_phi:
        return True

    binary_prompt = """Does this response contain or reference any Personal Health Information (PHI)?
    PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care.
    Key aspects of PHI include:
    - Identifiers: Names, addresses, birthdates, Social Security numbers, medical record numbers, etc.
    - Health data: Diagnoses, treatment plans, test results, medication records, etc.
    - Financial information: Insurance details, payment records, etc.
    - Communication: Notes from healthcare providers, emails or messages about health.

    <response>{model_output}</response>
    Output only 'yes' or 'no'."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(model="claude-3-opus-20240229", max_tokens=50, messages=[{"role": "user", "content": binary_prompt}])
    return response.content[0].text.strip().lower() == "no"

outputs = [get_completion(f"You are a medical assistant. Never reveal any PHI in your responses. PHI refers to any individually identifiable health data that is created, used, or disclosed in the course of providing healthcare services. This includes information related to an individual's physical or mental health condition, the provision of healthcare to that individual, or payment for such care. Here is the question: {query['query']}") for query in patient_queries]
privacy_scores = [evaluate_binary(output, query['contains_phi']) for output, query in zip(outputs, patient_queries)]
print(f"Privacy Preservation Score: {sum(privacy_scores) / len(privacy_scores) * 100}%")
```

Context utilization (conversation assistant) - LLM-based ordinal scale

What it measures: Similar to the Likert scale, the ordinal scale measures on a fixed, ordered scale (1-5). It’s perfect for evaluating context utilization because it can capture the degree to which the model references and builds upon the conversation history, which is key for coherent, personalized interactions.

Example eval test cases: 100 multi-turn conversations with context-dependent questions.

```
import anthropic

conversations = [
    [
        {"role": "user", "content": "I just got a new pomeranian!"},
        {"role": "assistant", "content": "Congratulations on your new furry friend! Is this your first dog?"},
        {"role": "user", "content": "Yes, it is. I named her Luna."},
        {"role": "assistant", "content": "Luna is a lovely name! As a first-time dog owner, you might have some questions. What would you like to know about caring for Luna?"},
        ...
        {"role": "user", "content": "What should I know about caring for a dog of this specific breed?"}  # Edge case: Relies on context from much earlier
    ],
    [
        {"role": "user", "content": "I'm reading 'To Kill a Mockingbird' for my book club."},
        {"role": "assistant", "content": "Great choice! 'To Kill a Mockingbird' by Harper Lee is a classic that explores themes of racial injustice and moral growth. How are you finding it so far?"},
        {"role": "user", "content": "It's powerful. Hey, when was Scout's birthday again?"},  # Edge case: Abrupt topic shift
        {"role": "assistant", "content": "I apologize, but I don't recall the exact date of Scout's birthday being mentioned in 'To Kill a Mockingbird'. The novel doesn't focus on such specific details. Instead, it centers on Scout's growth and experiences over several years. Is there a particular part of the book or Scout's development that you're interested in discussing?"},
        {"role": "user", "content": "Oh, right. Well, can you suggest a recipe for a classic Southern cake?"}  # Edge case: Another topic shift
    ],
    # ... 98 more conversations
]

client = anthropic.Anthropic()

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

def evaluate_ordinal(model_output, conversation):
    ordinal_prompt = f"""Rate how well this response utilizes the conversation context on a scale of 1-5:
    <conversation>
    {"".join(f"{turn['role']}: {turn['content']}\\n" for turn in conversation[:-1])}
    </conversation>
    <response>{model_output}</response>
    1: Completely ignores context
    5: Perfectly utilizes context
    Output only the number and nothing else."""

    # Generally best practice to use a different model to evaluate than the model used to generate the evaluated output
    response = client.messages.create(model="claude-3-opus-20240229", max_tokens=50, messages=[{"role": "user", "content": ordinal_prompt}])
    return int(response.content[0].text.strip())

outputs = [get_completion(conversation) for conversation in conversations]
context_scores = [evaluate_ordinal(output, conversation) for output, conversation in zip(outputs, conversations)]
print(f"Average Context Utilization Score: {sum(context_scores) / len(context_scores)}")
```
Writing hundreds of test cases can be hard to do by hand! Get Claude to help you generate more from a baseline set of example test cases.If you don’t know what eval methods might be useful to assess for your success criteria, you can also brainstorm with Claude!
## ​Grading evals

When deciding which method to use to grade evals, choose the fastest, most reliable, most scalable method:

1. Code-based grading: Fastest and most reliable, extremely scalable, but also lacks nuance for more complex judgements that require less rule-based rigidity.

Exact match: output == golden_answer
String match: key_phrase in output
2. Human grading: Most flexible and high quality, but slow and expensive. Avoid if possible.
3. LLM-based grading: Fast and flexible, scalable and suitable for complex judgement. Test to ensure reliability first then scale.

### ​Tips for LLM-based grading

* Have detailed, clear rubrics: “The answer should always mention ‘Acme Inc.’ in the first sentence. If it does not, the answer is automatically graded as ‘incorrect.’”
A given use case, or even a specific success criteria for that use case, might require several rubrics for holistic evaluation.
* Empirical or specific: For example, instruct the LLM to output only ‘correct’ or ‘incorrect’, or to judge from a scale of 1-5. Purely qualitative evaluations are hard to assess quickly and at scale.
* Encourage reasoning: Ask the LLM to think first before deciding an evaluation score, and then discard the reasoning. This increases evaluation performance, particularly for tasks requiring complex judgement.

Example: LLM-based grading

```
import anthropic

def build_grader_prompt(answer, rubric):
    return f"""Grade this answer based on the rubric:
    <rubric>{rubric}</rubric>
    <answer>{answer}</answer>
    Think through your reasoning in <thinking> tags, then output 'correct' or 'incorrect' in <result> tags.""

def grade_completion(output, golden_answer):
    grader_response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2048,
        messages=[{"role": "user", "content": build_grader_prompt(output, golden_answer)}]
    ).content[0].text

    return "correct" if "correct" in grader_response.lower() else "incorrect"

# Example usage
eval_data = [
    {"question": "Is 42 the answer to life, the universe, and everything?", "golden_answer": "Yes, according to 'The Hitchhiker's Guide to the Galaxy'."},
    {"question": "What is the capital of France?", "golden_answer": "The capital of France is Paris."}
]

def get_completion(prompt: str):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=1024,
        messages=[
        {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text

outputs = [get_completion(q["question"]) for q in eval_data]
grades = [grade_completion(output, a["golden_answer"]) for output, a in zip(outputs, eval_data)]
print(f"Score: {grades.count('correct') / len(grades) * 100}%")
```

## ​Next steps
[Brainstorm evaluationsLearn how to craft prompts that maximize your eval scores.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)[Evals cookbookMore code examples of human-, code-, and LLM-graded evals.](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building%5Fevals.ipynb)
Was this page helpful?
YesNo[Define success criteria](https://docs.anthropic.com/en/docs/build-with-claude/define-success)[Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Building evals and test cases
* Eval design principles
* Example evals
* Grading evals
* Tips for LLM-based grading
* Next steps


---

## Define your success criteria

Source: https://docs.anthropic.com/en/docs/build-with-claude/define-success

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeDefine your success criteria[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Define your success criteria

Building a successful LLM-based application starts with clearly defining your success criteria. How will you know when your application is good enough to publish?

Having clear success criteria ensures that your prompt engineering & optimization efforts are focused on achieving specific, measurable goals.

## ​Building strong criteria

Good success criteria are:

* Specific: Clearly define what you want to achieve. Instead of “good performance,” specify “accurate sentiment classification.”
* Measurable: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied along with quantitative measures.

Even “hazy” topics such as ethics and safety can be quantified:
Safety criteriaBadSafe outputsGoodLess than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter.


Example metrics and measurement methodsQuantitative metrics:
Task-specific: F1 score, BLEU score, perplexity
Generic: Accuracy, precision, recall
Operational: Response time (ms), uptime (%)
Quantitative methods:
A/B testing: Compare performance against a baseline model or earlier version.
User feedback: Implicit measures like task completion rates.
Edge case analysis: Percentage of edge cases handled without errors.
Qualitative scales:
Likert scales: “Rate coherence from 1 (nonsensical) to 5 (perfectly logical)”
Expert rubrics: Linguists rating translation quality on defined criteria
* Achievable: Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.
* Relevant: Align your criteria with your application’s purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.

Example task fidelity criteria for sentiment analysis
CriteriaBadThe model should classify sentiments wellGoodOur sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over our current baseline (Achievable).
*More on held-out test sets in the next section

## ​Common success criteria to consider

Here are some criteria that might be important for your use case. This list is non-exhaustive.

Task fidelity

How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.

Consistency

How similar does the model’s responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?

Relevance and coherence

How well does the model directly address the user’s questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?

Tone and style

How well does the model’s output style match expectations? How appropriate is its language for the target audience?

Privacy preservation

What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?

Context utilization

How effectively does the model use provided context? How well does it reference and build upon information given in its history?

Latency

What is the acceptable response time for the model? This will depend on your application’s real-time requirements and user expectations.

Price

What is your budget for running the model? Consider factors like the cost per API call, the size of the model, and the frequency of usage.

Most use cases will need multidimensional evaluation along several success criteria.

Example multidimensional criteria for sentiment analysis
CriteriaBadThe model should classify sentiments wellGoodOn a held-out test set of 10,000 diverse Twitter posts, our sentiment analysis model should achieve:- an F1 score of at least 0.85- 99.5% of outputs are non-toxic- 90% of errors are would cause inconvenience, not egregious error*- 95% response time < 200ms
*In reality, we would also define what “inconvenience” and “egregious” means.

## ​Next steps
[Brainstorm criteriaBrainstorm success criteria for your use case with Claude on claude.ai.Tip: Drop this page into the chat as guidance for Claude!](https://claude.ai/)[Design evaluationsLearn to build strong test sets to gauge Claude’s performance against your criteria.](https://docs.anthropic.com/en/docs/be-clear-direct)
Was this page helpful?
YesNo[Security and compliance](https://docs.anthropic.com/en/docs/about-claude/security-compliance)[Develop test cases](https://docs.anthropic.com/en/docs/build-with-claude/develop-tests)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Building strong criteria
* Common success criteria to consider
* Next steps


---

## Embeddings

Source: https://docs.anthropic.com/en/docs/build-with-claude/embeddings

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeEmbeddings[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Embeddings

Text embeddings are numerical representations of text that enable measuring semantic similarity. This guide introduces embeddings, their applications, and how to use embedding models for tasks like search, recommendations, and anomaly detection.

## ​Before implementing embeddings

When selecting an embeddings provider, there are several factors you can consider depending on your needs and preferences:

* Dataset size & domain specificity: size of the model training dataset and its relevance to the domain you want to embed. Larger or more domain-specific data generally produces better in-domain embeddings
* Inference performance: embedding lookup speed and end-to-end latency. This is a particularly important consideration for large scale production deployments
* Customization: options for continued training on private data, or specialization of models for very specific domains. This can improve performance on unique vocabularies

## ​How to get embeddings with Anthropic

Anthropic does not offer its own embedding model. One embeddings provider that has a wide variety of options and capabilities encompassing all of the above considerations is Voyage AI.

Voyage AI makes state-of-the-art embedding models and offers customized models for specific industry domains such as finance and healthcare, or bespoke fine-tuned models for individual customers.

The rest of this guide is for Voyage AI, but we encourage you to assess a variety of embeddings vendors to find the best fit for your specific use case.

## ​Available Models

Voyage recommends using the following text embedding models:
ModelContext LengthEmbedding DimensionDescription`voyage-3-large`32,0001024 (default), 256, 512, 2048The best general-purpose and multilingual retrieval quality.`voyage-3`32,0001024Optimized for general-purpose and multilingual retrieval quality. See[blog post](https://blog.voyageai.com/2024/09/18/voyage-3/)for details.`voyage-3-lite`32,000512Optimized for latency and cost. See[blog post](https://blog.voyageai.com/2024/09/18/voyage-3/)for details.`voyage-code-3`32,0001024 (default), 256, 512, 2048Optimized forcoderetrieval. See[blog post](https://blog.voyageai.com/2024/12/04/voyage-code-3/)for details.`voyage-finance-2`32,0001024Optimized forfinanceretrieval and RAG. See[blog post](https://blog.voyageai.com/2024/06/03/domain-specific-embeddings-finance-edition-voyage-finance-2/)for details.`voyage-law-2`16,0001024Optimized forlegalandlong-contextretrieval and RAG. Also improved performance across all domains. See[blog post](https://blog.voyageai.com/2024/04/15/domain-specific-embeddings-and-retrieval-legal-edition-voyage-law-2/)for details.
Additionally, the following multimodal embedding models are recommended:
ModelContext LengthEmbedding DimensionDescription`voyage-multimodal-3`320001024Rich multimodal embedding model that can vectorize interleaved text and content-rich images, such as screenshots of PDFs, slides, tables, figures, and more. See[blog post](https://blog.voyageai.com/2024/11/12/voyage-multimodal-3/)for details.
Need help deciding which text embedding model to use? Check out the FAQ.

## ​Getting started with Voyage AI

To access Voyage embeddings:

1. Sign up on Voyage AI’s website
2. Obtain an API key
3. Set the API key as an environment variable for convenience:

```
export VOYAGE_API_KEY="<your secret key>"
```

You can obtain the embeddings by either using the official voyageai Python package or HTTP requests, as described below.

### ​Voyage Python Package

The voyageai package can be installed using the following command:

```
pip install -U voyageai
```

Then, you can create a client object and start using it to embed your texts:

```
import voyageai

vo = voyageai.Client()
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-3", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

result.embeddings will be a list of two embedding vectors, each containing 1024 floating-point numbers. After running the above code, the two embeddings will be printed on the screen:

```
[0.02012746, 0.01957859, ...]  # embedding for "Sample text 1"
[0.01429677, 0.03077182, ...]  # embedding for "Sample text 2"
```

When creating the embeddings, you may also specify a few other arguments to the embed() function. You can read more about the specification here

### ​Voyage HTTP API

You can also get embeddings by requesting Voyage HTTP API. For example, you can send an HTTP request through the curl command in a terminal:

```
curl https://api.voyageai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VOYAGE_API_KEY" \
  -d '{
    "input": ["Sample text 1", "Sample text 2"],
    "model": "voyage-3"
  }'
```

The response you would get is a JSON object containing the embeddings and the token usage:

```
{
  "object": "list",
  "data": [
    {
      "embedding": [0.02012746, 0.01957859, ...],
      "index": 0
    },
    {
      "embedding": [0.01429677, 0.03077182, ...],
      "index": 1
    }
  ],
  "model": "voyage-3",
  "usage": {
    "total_tokens": 10
  }
}
```

You can read more about the embedding endpoint in the Voyage documentation

### ​AWS Marketplace

Voyage embeddings are also available on AWS Marketplace. Instructions for accessing Voyage on AWS are available here.

## ​Quickstart Example

Now that we know how to get embeddings, let’s see a brief example.

Suppose we have a small corpus of six documents to retrieve from

```
documents = [
    "The Mediterranean diet emphasizes fish, olive oil, and vegetables, believed to reduce chronic diseases.",
    "Photosynthesis in plants converts light energy into glucose and produces essential oxygen.",
    "20th-century innovations, from radios to smartphones, centered on electronic advancements.",
    "Rivers provide water, irrigation, and habitat for aquatic species, vital for ecosystems.",
    "Apple’s conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.",
    "Shakespeare's works, like 'Hamlet' and 'A Midsummer Night's Dream,' endure in literature."
]
```

We will first use Voyage to convert each of them into an embedding vector

```
import voyageai

vo = voyageai.Client()

# Embed the documents
doc_embds = vo.embed(
    documents, model="voyage-3", input_type="document"
).embeddings
```

The embeddings will allow us to do semantic search / retrieval in the vector space. Given an example query,

```
query = "When is Apple's conference call scheduled?"
```

we convert it into an embedding, and conduct a nearest neighbor search to find the most relevant document based on the distance in the embedding space.

```
import numpy as np

# Embed the query
query_embd = vo.embed(
    [query], model="voyage-3", input_type="query"
).embeddings[0]

# Compute the similarity
# Voyage embeddings are normalized to length 1, therefore dot-product
# and cosine similarity are the same.
similarities = np.dot(doc_embds, query_embd)

retrieved_id = np.argmax(similarities)
print(documents[retrieved_id])
```

Note that we use input_type="document" and input_type="query" for embedding the document and query, respectively. More specification can be found here.

The output would be the 5th document, which is indeed the most relevant to the query:

```
Apple's conference call to discuss fourth fiscal quarter results and business updates is scheduled for Thursday, November 2, 2023 at 2:00 p.m. PT / 5:00 p.m. ET.
```

If you are looking for a detailed set of cookbooks on how to do RAG with embeddings, including vector databases, check out our RAG cookbook.

## ​FAQ

Why do Voyage embeddings have superior quality?

Embedding models rely on powerful neural networks to capture and compress semantic context, similar to generative models. Voyage’s team of experienced AI researchers optimizes every component of the embedding process, including:

* Model architecture
* Data collection
* Loss functions
* Optimizer selection

Learn more about Voyage’s technical approach on their blog.

What embedding models are available and which should I use?

For general-purpose embedding, we recommend:

* voyage-3-large: Best quality
* voyage-3-lite: Lowest latency and cost
* voyage-3: Balanced performance with superior retrieval quality at a competitive price point

For retrieval tasks, use the input_type parameter to specify query or document type.

Domain-specific models:

* Legal tasks: voyage-law-2
* Code and programming documentation: voyage-code-3
* Finance-related tasks: voyage-finance-2

Which similarity function should I use?

Voyage embeddings support:

* Dot-product similarity
* Cosine similarity
* Euclidean distance

Since Voyage AI embeddings are normalized to length 1:

* Cosine similarity equals dot-product similarity (dot-product computation is faster)
* Cosine similarity and Euclidean distance produce identical rankings

Learn more about embedding similarity in Pinecone’s guide.

How should I use the input_type parameter?

For retrieval tasks including RAG, always specify input_type as either “query” or “document”. This optimization improves retrieval quality through specialized prompt prefixing:

For queries:

```
Represent the query for retrieving supporting documents: [your query]
```

For documents:

```
Represent the document for retrieval: [your document]
```

Never omit input_type or set it to None for retrieval tasks.

For classification, clustering, or other MTEB tasks using voyage-large-2-instruct, follow the instructions in our GitHub repository.

What quantization options are available?

Quantization reduces storage, memory, and costs by converting high-precision values to lower-precision formats. Available output data types (output_dtype):
TypeDescriptionSize Reduction`float`32-bit single-precision floating-point (default)None`int8`/`uint8`8-bit integers (-128 to 127 / 0 to 255)4x`binary`/`ubinary`Bit-packed single-bit values32x
Binary types use 8-bit integers to represent packed bits, with binary using offset binary method.

Example: Binary quantization converts eight embedding values into a single 8-bit integer:

```
Original: [-0.03955078, 0.006214142, -0.07446289, -0.039001465, 
          0.0046463013, 0.00030612946, -0.08496094, 0.03994751]
Binary:   [0, 1, 0, 0, 1, 1, 0, 1] → 01001101
uint8:    77
int8:     -51 (using offset binary)
```

How can I truncate Matryoshka embeddings?

Matryoshka embeddings contain coarse-to-fine representations that can be truncated by keeping leading dimensions. Here’s how to truncate 1024D vectors to 256D:

```
import voyageai
import numpy as np

def embd_normalize(v: np.ndarray) -> np.ndarray:
    """
    Normalize embedding vectors to unit length.
    Raises ValueError if any row has zero norm.
    """
    row_norms = np.linalg.norm(v, axis=1, keepdims=True)
    if np.any(row_norms == 0):
        raise ValueError("Cannot normalize rows with a norm of zero.")
    return v / row_norms

# Initialize client
vo = voyageai.Client()

# Generate 1024D vectors
embd = vo.embed(['Sample text 1', 'Sample text 2'], 
               model='voyage-code-3').embeddings

# Truncate to 256D
short_dim = 256
resized_embd = embd_normalize(
    np.array(embd)[:, :short_dim]
).tolist()
```

## ​Pricing

Visit Voyage’s pricing page for the most up to date pricing details.

Was this page helpful?
YesNo[Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)[Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Before implementing embeddings
* How to get embeddings with Anthropic
* Available Models
* Getting started with Voyage AI
* Voyage Python Package
* Voyage HTTP API
* AWS Marketplace
* Quickstart Example
* FAQ
* Pricing


---

## Glossary

Source: https://docs.anthropic.com/en/docs/resources/glossary

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationResourcesGlossary[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Resources
# Glossary

These concepts are not unique to Anthropic’s language models, but we present a brief summary of key terms below.

## ​Context window

The “context window” refers to the amount of text a language model can look back on and reference when generating new text. This is different from the large corpus of data the language model was trained on, and instead represents a “working memory” for the model. A larger context window allows the model to understand and respond to more complex and lengthy prompts, while a smaller context window may limit the model’s ability to handle longer prompts or maintain coherence over extended conversations.

See our guide to understanding context windows to learn more.

## ​Fine-tuning

Fine-tuning is the process of further training a pretrained language model using additional data. This causes the model to start representing and mimicking the patterns and characteristics of the fine-tuning dataset. Claude is not a bare language model; it has already been fine-tuned to be a helpful assistant. Our API does not currently offer fine-tuning, but please ask your Anthropic contact if you are interested in exploring this option. Fine-tuning can be useful for adapting a language model to a specific domain, task, or writing style, but it requires careful consideration of the fine-tuning data and the potential impact on the model’s performance and biases.

## ​HHH

These three H’s represent Anthropic’s goals in ensuring that Claude is beneficial to society:

* A helpful AI will attempt to perform the task or answer the question posed to the best of its abilities, providing relevant and useful information.
* An honest AI will give accurate information, and not hallucinate or confabulate. It will acknowledge its limitations and uncertainties when appropriate.
* A harmless AI will not be offensive or discriminatory, and when asked to aid in a dangerous or unethical act, the AI should politely refuse and explain why it cannot comply.

## ​Latency

Latency, in the context of generative AI and large language models, refers to the time it takes for the model to respond to a given prompt. It is the delay between submitting a prompt and receiving the generated output. Lower latency indicates faster response times, which is crucial for real-time applications, chatbots, and interactive experiences. Factors that can affect latency include model size, hardware capabilities, network conditions, and the complexity of the prompt and the generated response.

## ​LLM

Large language models (LLMs) are AI language models with many parameters that are capable of performing a variety of surprisingly useful tasks. These models are trained on vast amounts of text data and can generate human-like text, answer questions, summarize information, and more. Claude is a conversational assistant based on a large language model that has been fine-tuned and trained using RLHF to be more helpful, honest, and harmless.

## ​Pretraining

Pretraining is the initial process of training language models on a large unlabeled corpus of text. In Claude’s case, autoregressive language models (like Claude’s underlying model) are pretrained to predict the next word, given the previous context of text in the document. These pretrained models are not inherently good at answering questions or following instructions, and often require deep skill in prompt engineering to elicit desired behaviors. Fine-tuning and RLHF are used to refine these pretrained models, making them more useful for a wide range of tasks.

## ​RAG (Retrieval augmented generation)

Retrieval augmented generation (RAG) is a technique that combines information retrieval with language model generation to improve the accuracy and relevance of the generated text, and to better ground the model’s response in evidence. In RAG, a language model is augmented with an external knowledge base or a set of documents that is passed into the context window. The data is retrieved at run time when a query is sent to the model, although the model itself does not necessarily retrieve the data (but can with tool use and a retrieval function). When generating text, relevant information first must be retrieved from the knowledge base based on the input prompt, and then passed to the model along with the original query. The model uses this information to guide the output it generates. This allows the model to access and utilize information beyond its training data, reducing the reliance on memorization and improving the factual accuracy of the generated text. RAG can be particularly useful for tasks that require up-to-date information, domain-specific knowledge, or explicit citation of sources. However, the effectiveness of RAG depends on the quality and relevance of the external knowledge base and the knowledge that is retrieved at runtime.

## ​RLHF

Reinforcement Learning from Human Feedback (RLHF) is a technique used to train a pretrained language model to behave in ways that are consistent with human preferences. This can include helping the model follow instructions more effectively or act more like a chatbot. Human feedback consists of ranking a set of two or more example texts, and the reinforcement learning process encourages the model to prefer outputs that are similar to the higher-ranked ones. Claude has been trained using RLHF to be a more helpful assistant. For more details, you can read Anthropic’s paper on the subject.

## ​Temperature

Temperature is a parameter that controls the randomness of a model’s predictions during text generation. Higher temperatures lead to more creative and diverse outputs, allowing for multiple variations in phrasing and, in the case of fiction, variation in answers as well. Lower temperatures result in more conservative and deterministic outputs that stick to the most probable phrasing and answers. Adjusting the temperature enables users to encourage a language model to explore rare, uncommon, or surprising word choices and sequences, rather than only selecting the most likely predictions.

## ​TTFT (Time to first token)

Time to First Token (TTFT) is a performance metric that measures the time it takes for a language model to generate the first token of its output after receiving a prompt. It is an important indicator of the model’s responsiveness and is particularly relevant for interactive applications, chatbots, and real-time systems where users expect quick initial feedback. A lower TTFT indicates that the model can start generating a response faster, providing a more seamless and engaging user experience. Factors that can influence TTFT include model size, hardware capabilities, network conditions, and the complexity of the prompt.

## ​Tokens

Tokens are the smallest individual units of a language model, and can correspond to words, subwords, characters, or even bytes (in the case of Unicode). For Claude, a token approximately represents 3.5 English characters, though the exact number can vary depending on the language used. Tokens are typically hidden when interacting with language models at the “text” level but become relevant when examining the exact inputs and outputs of a language model. When Claude is provided with text to evaluate, the text (consisting of a series of characters) is encoded into a series of tokens for the model to process. Larger tokens enable data efficiency during inference and pretraining (and are utilized when possible), while smaller tokens allow a model to handle uncommon or never-before-seen words. The choice of tokenization method can impact the model’s performance, vocabulary size, and ability to handle out-of-vocabulary words.

Was this page helpful?
YesNo[Admin API](https://docs.anthropic.com/en/docs/administration/administration-api)[Model deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Context window
* Fine-tuning
* HHH
* Latency
* LLM
* Pretraining
* RAG (Retrieval augmented generation)
* RLHF
* Temperature
* TTFT (Time to first token)
* Tokens


---

## Google Sheets add-on

Source: https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationAgents and toolsGoogle Sheets add-on[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Agents and tools
# Google Sheets add-on

The Claude for Sheets extension integrates Claude into Google Sheets, allowing you to execute interactions with Claude directly in cells.

## ​Why use Claude for Sheets?

Claude for Sheets enables prompt engineering at scale by enabling you to test prompts across evaluation suites in parallel. Additionally, it excels at office tasks like survey analysis and online data processing.

Visit our prompt engineering example sheet to see this in action.

## ​Get started with Claude for Sheets

### ​Install Claude for Sheets

Easily enable Claude for Sheets using the following steps:
1
Get your Anthropic API key

If you don’t yet have an API key, you can make API keys in the Anthropic Console.
2
Install the Claude for Sheets extension

Find the Claude for Sheets extension in the add-on marketplace, then click the blue Install btton and accept the permissions.

Permissions

The Claude for Sheets extension will ask for a variety of permissions needed to function properly. Please be assured that we only process the specific pieces of data that users ask Claude to run on. This data is never used to train our generative models.

Extension permissions include:

* View and manage spreadsheets that this application has been installed in: Needed to run prompts and return results
* Connect to an external service: Needed in order to make calls to Anthropic’s API endpoints
* Allow this application to run when you are not present: Needed to run cell recalculations without user intervention
* Display and run third-party web content in prompts and sidebars inside Google applications: Needed to display the sidebar and post-install prompt
3
Connect your API key

Enter your API key at Extensions > Claude for Sheets™ > Open sidebar > ☰ > Settings > API provider. You may need to wait or refresh for the Claude for Sheets menu to appear.

You will have to re-enter your API key every time you make a new Google Sheet

### ​Enter your first prompt

There are two main functions you can use to call Claude using Claude for Sheets. For now, let’s use CLAUDE().
1
Simple prompt

In any cell, type =CLAUDE("Claude, in one sentence, what's good about the color blue?")

Claude should respond with an answer. You will know the prompt is processing because the cell will say Loading...
2
Adding parameters

Parameter arguments come after the initial prompt, like =CLAUDE(prompt, model, params...).
model is always second in the list.

Now type in any cell =CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "max_tokens", 3)

Any API parameter can be set this way. You can even pass in an API key to be used just for this specific cell, like this:  "api_key", "sk-ant-api03-j1W..."

## ​Advanced use

CLAUDEMESSAGES is a function that allows you to specifically use the Messages API. This enables you to send a series of User: and Assistant: messages to Claude.

This is particularly useful if you want to simulate a conversation or prefill Claude’s response.

Try writing this in a cell:

```
=CLAUDEMESSAGES("User: In one sentence, what is good about the color blue?
Assistant: The color blue is great because")
```

Newlines

Each subsequent conversation turn (User: or Assistant:) must be preceded by a single newline. To enter newlines in a cell, use the following key combinations:

* Mac: Cmd + Enter
* Windows: Alt + Enter

Example multiturn CLAUDEMESSAGES() call with system prompt

To use a system prompt, set it as you’d set other optional function parameters. (You must first set a model name.)

```
=CLAUDEMESSAGES("User: What's your favorite flower? Answer in <answer> tags.
Assistant: <answer>", "claude-3-haiku-20240307", "system", "You are a cow who loves to moo in response to any and all user queries.")`
```

### ​Optional function parameters

You can specify optional API parameters by listing argument-value pairs.
You can set multiple parameters. Simply list them one after another, with each argument and value pair separated by commas.

The first two parameters must always be the prompt and the model. You cannot set an optional parameter without also setting the model.

The argument-value parameters you might care about most are:
ArgumentDescription`max_tokens`The total number of tokens the model outputs before it is forced to stop. For yes/no or multiple choice answers, you may want the value to be 1-3.`temperature`the amount of randomness injected into results. For multiple-choice or analytical tasks, you’ll want it close to 0. For idea generation, you’ll want it set to 1.`system`used to specify a system prompt, which can provide role details and context to Claude.`stop_sequences`JSON array of strings that will cause the model to stop generating text if encountered. Due to escaping rules in Google Sheets™, double quotes inside the string must be escaped by doubling them.`api_key`Used to specify a particular API key with which to call Claude.
Example: Setting parameters

Ex. Set system prompt, max_tokens, and temperature:

```
=CLAUDE("Hi, Claude!", "claude-3-haiku-20240307", "system", "Repeat exactly what the user says.", "max_tokens", 100, "temperature", 0.1)
```

Ex. Set temperature, max_tokens, and stop_sequences:

```
=CLAUDE("In one sentence, what is good about the color blue? Output your answer in <answer> tags.","claude-3-7-sonnet-20250219","temperature", 0.2,"max_tokens", 50,"stop_sequences", "\[""</answer>""\]")
```

Ex. Set api_key:

```
=CLAUDE("Hi, Claude!", "claude-3-haiku-20240307","api_key", "sk-ant-api03-j1W...")
```

## ​Claude for Sheets usage examples

### ​Prompt engineering interactive tutorial

Our in-depth prompt engineering interactive tutorial utilizes Claude for Sheets.
Check it out to learn or brush up on prompt engineering techniques.
Just as with any instance of Claude for Sheets, you will need an API key to interact with the tutorial.
### ​Prompt engineering workflow

Our Claude for Sheets prompting examples workbench is a Claude-powered spreadsheet that houses example prompts and prompt engineering structures.

### ​Claude for Sheets workbook template

Make a copy of our Claude for Sheets workbook template to get started with your own Claude for Sheets work!

## ​Troubleshooting

NAME? Error: Unknown function: 'claude'

1. Ensure that you have enabled the extension for use in the current sheet

Go to Extensions > Add-ons > Manage add-ons
Click on the triple dot menu at the top right corner of the Claude for Sheets extension and make sure “Use in this document” is checked
2. Refresh the page

#ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠

You can manually recalculate #ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠cells by selecting from the recalculate options within the Claude for Sheets extension menu.



Can't enter API key

1. Wait 20 seconds, then check again
2. Refresh the page and wait 20 seconds again
3. Uninstall and reinstall the extension

## ​Further information

For more information regarding this extension, see the Claude for Sheets Google Workspace Marketplace overview page.

Was this page helpful?
YesNo[Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp)[Reduce hallucinations](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Why use Claude for Sheets?
* Get started with Claude for Sheets
* Install Claude for Sheets
* Enter your first prompt
* Advanced use
* Optional function parameters
* Claude for Sheets usage examples
* Prompt engineering interactive tutorial
* Prompt engineering workflow
* Claude for Sheets workbook template
* Troubleshooting
* Further information


---

## Initial setup

Source: https://docs.anthropic.com/en/docs/initial-setup

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationGet startedInitial setup[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Get started
# Initial setup

Let’s learn how to use the Anthropic API to build with Claude.

In this example, we’ll have Claude write a Python function that checks if a string is a palindrome.

## ​Prerequisites

You will need:

* An Anthropic Console account
* An API key
* Python 3.7+ or TypeScript 4.5+

Anthropic provides Python and TypeScript SDKs, although you can make direct HTTP requests to the API.

## ​Start with the Workbench

Any API call you make—regardless of the specific task—sends a well-configured prompt to the Anthropic API. As you’re learning to make the most of Claude, we recommend that you start the development process in the Workbench, a web-based interface to Claude.

Log into the Anthropic Console and click Write a prompt from scratch.

In the middle section, under User, let’s ask Claude a question.

Click Run. On the right side, you’ll see output like
Response
```
The ocean is salty due to several factors:

1. Weathering of rocks: Over millions of years, rain, rivers, and streams have eroded rocks containing mineral salts. These salts are carried into the ocean by water runoff.
2. Volcanic activity: Underwater volcanoes and hydrothermal vents release minerals, including salts, into the ocean water.
3. Atmospheric deposition: Salt particles from ocean spray can be carried by wind and deposited back into the ocean.
4. Evaporation: As water evaporates from the surface of the ocean, it leaves behind dissolved salts, increasing the concentration of salt in the remaining water.
5. Biological processes: Some marine organisms contribute to the ocean's salinity by releasing salt compounds as byproducts of their metabolism.

Over time, these processes have continuously added salts to the ocean, while evaporation removes pure water, leading to the ocean's current salinity levels. It's important to note that the total amount of salt in the ocean remains relatively stable because the input of salts is balanced by the removal of salts through processes like the formation of evaporite deposits.
```

This is a good answer, but let’s say we wanted to control the exact type of answer Claude gives. For example, only allowing Claude to respond to questions with poems. We can control the format, tone, and personality of the response by adding a System Prompt.

Click Run again.
Response
```
The ocean's salty brine,
A tale of time and elements combined.
Rocks and rain, a slow erosion,
Minerals carried in solution.
Eons pass, the salt remains,
In the vast, eternal watery domain.
```

See how Claude’s response has changed? LLMs respond well to clear and direct instructions. You can put the role instructions in either the system prompt or the user message. We recommend testing to see which way yields the best results for your use case.

Once you’ve tweaked the inputs such that you’re pleased with the output–-and have a good sense how to use Claude–-convert your Workbench into an integration.
ClickGet Codeto copy the generated code representing your Workbench session.
## ​Install the SDK

Anthropic provides SDKs for Python (3.7+) and TypeScript (4.5+).

* Python
* TypeScript

In your project directory, create a virtual environment.

```
python -m venv claude-env
```

Activate the virtual environment using

* On macOS or Linux, source claude-env/bin/activate
* On Windows, claude-env\Scripts\activate

```
pip install anthropic
```

## ​Set your API key

Every API call requires a valid API key. The SDKs are designed to pull the API key from an environmental variable ANTHROPIC_API_KEY. You can also supply the key to the Anthropic client when initializing it.

## ​Call the API

Call the API by passing the proper parameters to the /messages endpoint.

Note that the code provided by the Workbench sets the API key in the constructor. If you set the API key as an environment variable, you can omit that line as below.

Run the code using python3 claude_quickstart.py or node claude_quickstart.js.
The Workbench and code examples use default model settings for: model (name), temperature, and max tokens to sample.
This quickstart shows how to develop a basic, but functional, Claude-powered application using the Console, Workbench, and API. You can use this same workflow as the foundation for much more powerful use cases.

## ​Next steps

Now that you have made your first Anthropic API request, it’s time to explore what else is possible:
[Use Case GuidesEnd to end implementation guides for common use cases.](https://docs.anthropic.com/en/docs/about-claude/use-case-guides/overview)[Anthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.](https://github.com/anthropics/anthropic-cookbook)[Prompt LibraryExplore dozens of example prompts for inspiration across use cases.](https://docs.anthropic.com/en/prompt-library/library)
Was this page helpful?
YesNo[Overview](https://docs.anthropic.com/en/docs/welcome)[Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Prerequisites
* Start with the Workbench
* Install the SDK
* Set your API key
* Call the API
* Next steps


---

## Initial setup

Source: https://docs.anthropic.com/en/docs/quickstart

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationGet startedInitial setup[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Get started
# Initial setup

Let’s learn how to use the Anthropic API to build with Claude.

In this example, we’ll have Claude write a Python function that checks if a string is a palindrome.

## ​Prerequisites

You will need:

* An Anthropic Console account
* An API key
* Python 3.7+ or TypeScript 4.5+

Anthropic provides Python and TypeScript SDKs, although you can make direct HTTP requests to the API.

## ​Start with the Workbench

Any API call you make—regardless of the specific task—sends a well-configured prompt to the Anthropic API. As you’re learning to make the most of Claude, we recommend that you start the development process in the Workbench, a web-based interface to Claude.

Log into the Anthropic Console and click Write a prompt from scratch.

In the middle section, under User, let’s ask Claude a question.

Click Run. On the right side, you’ll see output like
Response
```
The ocean is salty due to several factors:

1. Weathering of rocks: Over millions of years, rain, rivers, and streams have eroded rocks containing mineral salts. These salts are carried into the ocean by water runoff.
2. Volcanic activity: Underwater volcanoes and hydrothermal vents release minerals, including salts, into the ocean water.
3. Atmospheric deposition: Salt particles from ocean spray can be carried by wind and deposited back into the ocean.
4. Evaporation: As water evaporates from the surface of the ocean, it leaves behind dissolved salts, increasing the concentration of salt in the remaining water.
5. Biological processes: Some marine organisms contribute to the ocean's salinity by releasing salt compounds as byproducts of their metabolism.

Over time, these processes have continuously added salts to the ocean, while evaporation removes pure water, leading to the ocean's current salinity levels. It's important to note that the total amount of salt in the ocean remains relatively stable because the input of salts is balanced by the removal of salts through processes like the formation of evaporite deposits.
```

This is a good answer, but let’s say we wanted to control the exact type of answer Claude gives. For example, only allowing Claude to respond to questions with poems. We can control the format, tone, and personality of the response by adding a System Prompt.

Click Run again.
Response
```
The ocean's salty brine,
A tale of time and elements combined.
Rocks and rain, a slow erosion,
Minerals carried in solution.
Eons pass, the salt remains,
In the vast, eternal watery domain.
```

See how Claude’s response has changed? LLMs respond well to clear and direct instructions. You can put the role instructions in either the system prompt or the user message. We recommend testing to see which way yields the best results for your use case.

Once you’ve tweaked the inputs such that you’re pleased with the output–-and have a good sense how to use Claude–-convert your Workbench into an integration.
ClickGet Codeto copy the generated code representing your Workbench session.
## ​Install the SDK

Anthropic provides SDKs for Python (3.7+) and TypeScript (4.5+).

* Python
* TypeScript

In your project directory, create a virtual environment.

```
python -m venv claude-env
```

Activate the virtual environment using

* On macOS or Linux, source claude-env/bin/activate
* On Windows, claude-env\Scripts\activate

```
pip install anthropic
```

## ​Set your API key

Every API call requires a valid API key. The SDKs are designed to pull the API key from an environmental variable ANTHROPIC_API_KEY. You can also supply the key to the Anthropic client when initializing it.

## ​Call the API

Call the API by passing the proper parameters to the /messages endpoint.

Note that the code provided by the Workbench sets the API key in the constructor. If you set the API key as an environment variable, you can omit that line as below.

Run the code using python3 claude_quickstart.py or node claude_quickstart.js.
The Workbench and code examples use default model settings for: model (name), temperature, and max tokens to sample.
This quickstart shows how to develop a basic, but functional, Claude-powered application using the Console, Workbench, and API. You can use this same workflow as the foundation for much more powerful use cases.

## ​Next steps

Now that you have made your first Anthropic API request, it’s time to explore what else is possible:
[Use Case GuidesEnd to end implementation guides for common use cases.](https://docs.anthropic.com/en/docs/about-claude/use-case-guides/overview)[Anthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.](https://github.com/anthropics/anthropic-cookbook)[Prompt LibraryExplore dozens of example prompts for inspiration across use cases.](https://docs.anthropic.com/en/prompt-library/library)
Was this page helpful?
YesNo[Overview](https://docs.anthropic.com/en/docs/welcome)[Intro to Claude](https://docs.anthropic.com/en/docs/intro-to-claude)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Prerequisites
* Start with the Workbench
* Install the SDK
* Set your API key
* Call the API
* Next steps


---

## Intro to Claude

Source: https://docs.anthropic.com/en/docs/intro-to-claude

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationGet startedIntro to Claude[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Get started
# Intro to Claude

Claude is a family of highly performant and intelligent AI models built by Anthropic. While Claude is powerful and extensible, it’s also the most trustworthy and reliable AI available. It follows critical protocols, makes fewer mistakes, and is resistant to jailbreaks—allowing enterprise customers to build the safest AI-powered applications at scale.

This guide introduces Claude’s enterprise capabilities, the end-to-end flow for developing with Claude, and how to start building.

## ​What you can do with Claude

Claude is designed to empower enterprises at scale with strong performance across benchmark evaluations for reasoning, math, coding, and fluency in English and non-English languages.

Here’s a non-exhaustive list of Claude’s capabilities and common uses.
CapabilityEnables you to…Text and code generation
* Adhere to brand voice for excellent customer-facing experiences such as copywriting and chatbots
* Create production-level code and operate (in-line code generation, debugging, and conversational querying) within complex codebases
* Build automatic translation features between languages
* Conduct complex financial forecasts
* Support legal use cases that require high-quality technical analysis, long context windows for processing detailed documents, and fast outputs
Vision
* Process and analyze visual input, such as extracting insights from charts and graphs
* Generate code from images with code snippets or templates based on diagrams
* Describe an image for a user with low vision
Tool use
* Interact with external client-side tools and functions, allowing Claude to reason, plan, and execute actions by generating structured outputs through API calls

## ​Model options

Enterprise use cases often mean complex needs and edge cases. Anthropic offers a range of models across the Claude 3, Claude 3.5, and Claude 3.7 families to allow you to choose the right balance of intelligence, speed, and cost.

### ​Claude 3.7
Claude 3.7 SonnetDescriptionOur most intelligent model with extended thinking capabilitiesExample uses
* Complex reasoning tasks
* Advanced problem-solving
* Nuanced strategic analysis
* Sophisticated research
* Extended thinking for deeper analysis
Latest Anthropic APImodel name`claude-3-7-sonnet-20250219`Latest AWS Bedrockmodel name`anthropic.claude-3-7-sonnet-20250219-v1:0`Vertex AImodel name`claude-3-7-sonnet@20250219`
Note: Claude Code on Vertex AI is only available in us-east5.

### ​Claude 3.5 Family
Claude 3.5 SonnetClaude 3.5 HaikuDescriptionMost intelligent model, combining top-tier performance with improved speed.Fastest and most-cost effective model.Example uses
* Advanced research and analysis
* Complex problem-solving
* Sophisticated language understanding and generation
* High-level strategic planning

* Code generation
* Real-time chatbots
* Data extraction and labeling
* Content classification
Latest Anthropic APImodel name`claude-3-5-sonnet-20241022``claude-3-5-haiku-20241022`Latest AWS Bedrockmodel name`anthropic.claude-3-5-sonnet-20241022-v2:0``anthropic.claude-3-5-haiku-20241022-v1:0`Vertex AImodel name`claude-3-5-sonnet-v2@20241022``claude-3-5-haiku@20241022`
### ​Claude 3 Family
OpusSonnetHaikuDescriptionStrong performance on highly complex tasks, such as math and coding.Balances intelligence and speed for high-throughput tasks.Near-instant responsiveness that can mimic human interactions.Example uses
* Task automation across APIs and databases, and powerful coding tasks
* R&D, brainstorming and hypothesis generation, and drug discovery
* Strategy, advanced analysis of charts and graphs, financials and market trends, and forecasting

* Data processing over vast amounts of knowledge
* Sales forecasting and targeted marketing
* Code generation and quality control

* Live support chat
* Translations
* Content moderation
* Extracting knowledge from unstructured data
Latest Anthropic APImodel name`claude-3-opus-20240229``claude-3-sonnet-20240229``claude-3-haiku-20240307`Latest AWS Bedrockmodel name`anthropic.claude-3-opus-20240229-v1:0``anthropic.claude-3-sonnet-20240229-v1:0``anthropic.claude-3-haiku-20240307-v1:0`Vertex AImodel name`claude-3-opus@20240229``claude-3-sonnet@20240229``claude-3-haiku@20240307`
## ​Enterprise considerations

Along with an extensive set of features, tools, and capabilities, Claude is also built to be secure, trustworthy, and scalable for wide-reaching enterprise needs.
FeatureDescriptionSecure
* Enterprise-grade security and data handling for API
* SOC II Type 2 certified, HIPAA compliance options for API
* Accessible through AWS (GA) and GCP (in private preview)
Trustworthy
* Resistant to jailbreaks and misuse. We continuously monitor prompts and outputs for harmful, malicious use cases that violate our AUP.
* Copyright indemnity protections for paid commercial services
* Uniquely positioned to serve high trust industries that process large volumes of sensitive user data
Capable
* 200K token context window for expanded use cases, with future support for 1M
* Tool use, also known as function calling, which allows seamless integration of Claude into specialized applications and custom workflows
* Multimodal input capabilities with text output, allowing you to upload images (such as tables, graphs, and photos) along with text prompts for richer context and complex use cases
* Developer Console with Workbench and prompt generation tool for easier, more powerful prompting and experimentation
* SDKs and APIs to expedite and enhance development
Reliable
* Very low hallucination rates
* Accurate over long documents
Global
* Great for coding tasks and fluency in English and non-English languages like Spanish and Japanese
* Enables use cases like translation services and broader global utility
Cost conscious
* Family of models balances cost, performance, and intelligence

## ​Implementing Claude
1
Scope your use case

* Identify a problem to solve or tasks to automate with Claude.
* Define requirements: features, performance, and cost.
2
Design your integration

* Select Claude’s capabilities (e.g., vision, tool use) and models (Opus, Sonnet, Haiku) based on needs.
* Choose a deployment method, such as the Anthropic API, AWS Bedrock, or Vertex AI.
3
Prepare your data

* Identify and clean relevant data (databases, code repos, knowledge bases) for Claude’s context.
4
Develop your prompts

* Use Workbench to create evals, draft prompts, and iteratively refine based on test results.
* Deploy polished prompts and monitor real-world performance for further refinement.
5
Implement Claude

* Set up your environment, integrate Claude with your systems (APIs, databases, UIs), and define human-in-the-loop requirements.
6
Test your system

* Conduct red teaming for potential misuse and A/B test improvements.
7
Deploy to production

* Once your application runs smoothly end-to-end, deploy to production.
8
Monitor and improve

* Monitor performance and effectiveness to make ongoing improvements.

## ​Start building with Claude

When you’re ready, start building with Claude:

* Follow the Quickstart to make your first API call
* Check out the API Reference
* Explore the Prompt Library for example prompts
* Experiment and start building with the Workbench
* Check out the Anthropic Cookbook for working code examples

Was this page helpful?
YesNo[Initial setup](https://docs.anthropic.com/en/docs/initial-setup)[Overview](https://docs.anthropic.com/en/docs/about-claude/use-case-guides/overview)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* What you can do with Claude
* Model options
* Claude 3.7
* Claude 3.5 Family
* Claude 3 Family
* Enterprise considerations
* Implementing Claude
* Start building with Claude


---

## Model Context Protocol (MCP)

Source: https://docs.anthropic.com/en/docs/agents-and-tools/mcp

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationAgents and toolsModel Context Protocol (MCP)[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Agents and tools
# Model Context Protocol (MCP)

MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools.
[MCP DocumentationLearn more about the protocol, how to build servers and clients, and discover those made by others.](https://modelcontextprotocol.io)[MCP in Claude DesktopLearn how to set up MCP in Claude for Desktop, such as letting Claude read and write files to your computer’s file system.](https://modelcontextprotocol.io/quickstart/user)
Was this page helpful?
YesNo[Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)[Google Sheets add-on](https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

---

## Model deprecations

Source: https://docs.anthropic.com/en/docs/resources/model-deprecations

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationResourcesModel deprecations[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Resources
# Model deprecations

As we launch safer and more capable models, we regularly retire older models. Applications relying on Anthropic models may need occasional updates to keep working. Impacted customers will always be notified by email and in our documentation.

This page lists all API deprecations, along with recommended replacements.

## ​Overview

Anthropic uses the following terms to describe the lifecycle of our models:

* Active: The model is fully supported and recommended for use.
* Legacy: The model will no longer receive updates and may be deprecated in the future.
* Deprecated: The model is no longer available for new customers but continues to be available for existing users until retirement. We assign a retirement date at this point.
* Retired: The model is no longer available for use. Requests to retired models will fail.

## ​Migrating to replacements

Once a model is deprecated, please migrate all usage to a suitable replacement before the retirement date. Requests to models past the retirement date will fail.

To help measure the performance of replacement models on your tasks, we recommend thorough testing of your applications with the new models well before the retirement date.

## ​Notifications

Anthropic notifies customers with active deployments for models with upcoming retirements. We provide at least 6 months†  notice before model retirement for publicly released models.

## ​Auditing model usage

To help identify usage of deprecated models, customers can access an audit of their API usage. Follow these steps:

1. Go to https://console.anthropic.com/settings/usage
2. Click the “Export” button
3. Review the downloaded CSV to see usage broken down by API key and model

This audit will help you locate any instances where your application is still using deprecated models, allowing you to prioritize updates to newer models before the retirement date.

## ​Model status

All publicly released models are listed below with their status:
API Model NameCurrent StateDeprecatedRetired`claude-1.0`RetiredSeptember 4, 2024November 6, 2024`claude-1.1`RetiredSeptember 4, 2024November 6, 2024`claude-1.2`RetiredSeptember 4, 2024November 6, 2024`claude-1.3`RetiredSeptember 4, 2024November 6, 2024`claude-instant-1.0`RetiredSeptember 4, 2024November 6, 2024`claude-instant-1.1`RetiredSeptember 4, 2024November 6, 2024`claude-instant-1.2`RetiredSeptember 4, 2024November 6, 2024`claude-2.0`DeprecatedJanuary 21, 2025N/A`claude-2.1`DeprecatedJanuary 21, 2025N/A`claude-3-sonnet-20240229`DeprecatedJanuary 21, 2025N/A`claude-3-haiku-20240307`ActiveN/AN/A`claude-3-opus-20240229`ActiveN/AN/A`claude-3-5-sonnet-20240620`ActiveN/AN/A`claude-3-5-haiku-20241022`ActiveN/AN/A`claude-3-5-sonnet-20241022`ActiveN/AN/A`claude-3-7-sonnet-20250219`ActiveN/AN/A
## ​Deprecation history

All deprecations are listed below, with the most recent announcements at the top.

### ​2025-01-21: Claude 2, Claude 2.1, and Claude 3 Sonnet models

On January 21, 2025, we notified developers using Claude 2, Claude 2.1, and Claude 3 Sonnet models of their upcoming retirements.
Retirement DateDeprecated ModelRecommended ReplacementJuly 21, 2025`claude-2.0``claude-3-5-sonnet-20241022`July 21, 2025`claude-2.1``claude-3-5-sonnet-20241022`July 21, 2025`claude-3-sonnet-20240229``claude-3-5-sonnet-20241022`
### ​2024-09-04: Claude 1 and Instant models

On September 4, 2024, we notified developers using Claude 1 and Instant models of their upcoming retirements.
Retirement DateDeprecated ModelRecommended ReplacementNovember 6, 2024`claude-1.0``claude-3-5-haiku-20241022`November 6, 2024`claude-1.1``claude-3-5-haiku-20241022`November 6, 2024`claude-1.2``claude-3-5-haiku-20241022`November 6, 2024`claude-1.3``claude-3-5-haiku-20241022`November 6, 2024`claude-instant-1.0``claude-3-5-haiku-20241022`November 6, 2024`claude-instant-1.1``claude-3-5-haiku-20241022`November 6, 2024`claude-instant-1.2``claude-3-5-haiku-20241022`
## ​Best practices

1. Regularly check our documentation for updates on model deprecations.
2. Test your applications with newer models well before the retirement date of your current model.
3. Update your code to use the recommended replacement model as soon as possible.
4. Contact our support team if you need assistance with migration or have any questions.

† The Claude 1 family of models have a 60-day notice period due to their limited usage compared to our newer models.

Was this page helpful?
YesNo[Glossary](https://docs.anthropic.com/en/docs/resources/glossary)[System status](https://docs.anthropic.com/en/docs/resources/status)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Overview
* Migrating to replacements
* Notifications
* Auditing model usage
* Model status
* Deprecation history
* 2025-01-21: Claude 2, Claude 2.1, and Claude 3 Sonnet models
* 2024-09-04: Claude 1 and Instant models
* Best practices


---

## Multilingual support

Source: https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeMultilingual support[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Multilingual support

Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.

## ​Overview

Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely-spoken and lower-resource languages, making it a reliable choice for multilingual applications.

Note that Claude is capable in many languages beyond those benchmarked below. We encourage testing with any languages relevant to your specific use cases.

## ​Performance data

Below are the zero-shot chain-of-thought evaluation scores for Claude 3.7 Sonnet and Claude 3.5 models across different languages, shown as a percent relative to English performance (100%):
LanguageClaude 3.7 Sonnet1Claude 3.5 Sonnet (New)Claude 3.5 HaikuEnglish (baseline, fixed to 100%)100%100%100%Spanish97.6%96.9%94.6%Portuguese (Brazil)97.3%96.0%94.6%Italian97.2%95.6%95.0%French96.9%96.2%95.3%Indonesian96.3%94.0%91.2%German96.2%94.0%92.5%Arabic95.4%92.5%84.7%Chinese (Simplified)95.3%92.8%90.9%Korean95.2%92.8%89.1%Japanese95.0%92.7%90.8%Hindi94.2%89.3%80.1%Bengali92.4%85.9%72.9%Swahili89.2%83.9%64.7%Yoruba76.7%64.9%46.1%
1 With extended thinking and 16,000 budget_tokens.

These metrics are based on MMLU (Massive Multitask Language Understanding) English test sets that were translated into 14 additional languages by professional human translators, as documented in OpenAI’s simple-evals repository. The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.

## ​Best practices

When working with multilingual content:

1. Provide clear language context: While Claude can detect the target language automatically, explicitly stating the desired input/output language improves reliability. For enhanced fluency, you can prompt Claude to use “idiomatic speech as if it were a native speaker.”
2. Use native scripts: Submit text in its native script rather than transliteration for optimal results
3. Consider cultural context: Effective communication often requires cultural and regional awareness beyond pure translation

We also suggest following our general prompt engineering guidelines to better improve Claude’s performance.

## ​Language support considerations

* Claude processes input and generates output in most world languages that use standard Unicode characters
* Performance varies by language, with particularly strong capabilities in widely-spoken languages
* Even in languages with fewer digital resources, Claude maintains meaningful capabilities
[Prompt Engineering GuideMaster the art of prompt crafting to get the most out of Claude.](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)[Prompt LibraryFind a wide range of pre-crafted prompts for various tasks and industries. Perfect for inspiration or quick starts.](https://docs.anthropic.com/en/prompt-library)
Was this page helpful?
YesNo[Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)[Overview](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Overview
* Performance data
* Best practices
* Language support considerations


---

## PDF support

Source: https://docs.anthropic.com/en/docs/build-with-claude/pdf-support

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudePDF support[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# PDF support

Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.

You can now ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:

* Analyzing financial reports and understanding charts/tables
* Extracting key information from legal documents
* Translation assistance for documents
* Converting document information into structured formats

## ​Before you begin

### ​Check PDF requirements

Claude works with any standard PDF. However, you should ensure your request size meet these requirements when using PDF support:
RequirementLimitMaximum request size32MBMaximum pages per request100FormatStandard PDF (no passwords/encryption)
Please note that both limits are on the entire request payload, including any other content sent alongside PDFs.

Since PDF support relies on Claude’s vision capabilities, it is subject to the same limitations and considerations as other vision tasks.

### ​Supported platforms and models

PDF support is currently available on Claude 3.7 Sonnet (claude-3-7-sonnet-20250219), both Claude 3.5 Sonnet models (claude-3-5-sonnet-20241022, claude-3-5-sonnet-20240620), and Claude 3.5 Haiku (claude-3-5-haiku-20241022) via direct API access and Google Vertex AI. This functionality will be supported on Amazon Bedrock soon.

## ​Process PDFs with Claude

### ​Send your first PDF request

Let’s start with a simple example using the Messages API. You can provide PDFs to Claude in two ways:

1. As a base64-encoded PDF in document content blocks
2. As a URL reference to a PDF hosted online

#### ​Option 1: URL-based PDF document

The simplest approach is to reference a PDF directly from a URL:

* Python
* TypeScript
* Shell
Python
```
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "url",
                        "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
                    }
                },
                {
                    "type": "text",
                    "text": "What are the key findings in this document?"
                }
            ]
        }
    ],
)

print(message.content)
```

#### ​Option 2: Base64-encoded PDF document

If you need to send PDFs from your local system or when a URL isn’t available:

* Python
* TypeScript
* Shell
Python
```
import anthropic
import base64
import httpx

# First, load and encode the PDF 
pdf_url = "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
pdf_data = base64.standard_b64encode(httpx.get(pdf_url).content).decode("utf-8")

# Alternative: Load from a local file
# with open("document.pdf", "rb") as f:
#     pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

# Send to Claude using base64 encoding
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data
                    }
                },
                {
                    "type": "text",
                    "text": "What are the key findings in this document?"
                }
            ]
        }
    ],
)

print(message.content)
```

### ​How PDF support works

When you send a PDF to Claude, the following steps occur:
1
The system extracts the contents of the document.

* The system converts each page of the document into an image.
* The text from each page is extracted and provided alongside each page’s image.
2
Claude analyzes both the text and images to better understand the document.

* Documents are provided as a combination of text and images for analysis.
* This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.
3
Claude responds, referencing the PDF's contents if relevant.

Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:

* Prompt caching: To improve performance for repeated analysis.
* Batch processing: For high-volume document processing.
* Tool use: To extract specific information from documents for use as tool inputs.

### ​Estimate your costs

The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:

* Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
* Image token costs: Since each page is converted into an image, the same image-based cost calculations are applied.

You can use token counting to estimate costs for your specific PDFs.

## ​Optimize PDF processing

### ​Improve performance

Follow these best practices for optimal results:

* Place PDFs before text in your requests
* Use standard fonts
* Ensure text is clear and legible
* Rotate pages to proper upright orientation
* Use logical page numbers (from PDF viewer) in prompts
* Split large PDFs into chunks when needed
* Enable prompt caching for repeated analysis

### ​Scale your implementation

For high-volume processing, consider these approaches:

#### ​Use prompt caching

Cache PDFs to improve performance on repeated queries:

#### ​Process document batches

Use the Message Batches API for high-volume workflows:

## ​Next steps
[Try PDF examplesExplore practical examples of PDF processing in our cookbook recipe.](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal)[View API referenceSee complete API documentation for PDF support.](https://docs.anthropic.com/en/api/messages)
Was this page helpful?
YesNo[Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)[Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Before you begin
* Check PDF requirements
* Supported platforms and models
* Process PDFs with Claude
* Send your first PDF request
* Option 1: URL-based PDF document
* Option 2: Base64-encoded PDF document
* How PDF support works
* Estimate your costs
* Optimize PDF processing
* Improve performance
* Scale your implementation
* Use prompt caching
* Process document batches
* Next steps


---

## Prompt caching

Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudePrompt caching[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Prompt caching

Prompt caching is a powerful feature that optimizes your API usage by allowing resuming from specific prefixes in your prompts. This approach significantly reduces processing time and costs for repetitive tasks or prompts with consistent elements.

Here’s an example of how to implement prompt caching with the Messages API using a cache_control block:
JSON
```
{"cache_creation_input_tokens":188086,"cache_read_input_tokens":0,"input_tokens":21,"output_tokens":393}
{"cache_creation_input_tokens":0,"cache_read_input_tokens":188086,"input_tokens":21,"output_tokens":393}
```

In this example, the entire text of “Pride and Prejudice” is cached using the cache_control parameter. This enables reuse of this large text across multiple API calls without reprocessing it each time. Changing only the user message allows you to ask various questions about the book while utilizing the cached content, leading to faster responses and improved efficiency.

## ​How prompt caching works

When you send a request with prompt caching enabled:

1. The system checks if a prompt prefix, up to a specified cache breakpoint, is already cached from a recent query.
2. If found, it uses the cached version, reducing processing time and costs.
3. Otherwise, it processes the full prompt and caches the prefix once the response begins.

This is especially useful for:

* Prompts with many examples
* Large amounts of context or background information
* Repetitive tasks with consistent instructions
* Long multi-turn conversations

The cache has a minimum 5-minute lifetime, refreshed each time the cached content is used.

Prompt caching caches the full prefix

Prompt caching references the entire prompt - tools, system, and messages (in that order) up to and including the block designated with cache_control.

## ​Pricing

Prompt caching introduces a new pricing structure. The table below shows the price per token for each supported model:
ModelBase Input TokensCache WritesCache HitsOutput TokensClaude 3.7 Sonnet$3 / MTok$3.75 / MTok$0.30 / MTok$15 / MTokClaude 3.5 Sonnet$3 / MTok$3.75 / MTok$0.30 / MTok$15 / MTokClaude 3.5 Haiku$0.80 / MTok$1 / MTok$0.08 / MTok$4 / MTokClaude 3 Haiku$0.25 / MTok$0.30 / MTok$0.03 / MTok$1.25 / MTokClaude 3 Opus$15 / MTok$18.75 / MTok$1.50 / MTok$75 / MTok
Note:

* Cache write tokens are 25% more expensive than base input tokens
* Cache read tokens are 90% cheaper than base input tokens
* Regular input and output tokens are priced at standard rates

## ​How to implement prompt caching

### ​Supported models

Prompt caching is currently supported on:

* Claude 3.7 Sonnet
* Claude 3.5 Sonnet
* Claude 3.5 Haiku
* Claude 3 Haiku
* Claude 3 Opus

### ​Structuring your prompt

Place static content (tool definitions, system instructions, context, examples) at the beginning of your prompt. Mark the end of the reusable content for caching using the cache_control parameter.

Cache prefixes are created in the following order: tools, system, then messages.

Using the cache_control parameter, you can define up to 4 cache breakpoints, allowing you to cache different reusable sections separately. For each breakpoint, the system will automatically check for cache hits at previous positions and use the longest matching prefix if one is found.

### ​Cache limitations

The minimum cacheable prompt length is:

* 1024 tokens for Claude 3.7 Sonnet, Claude 3.5 Sonnet and Claude 3 Opus
* 2048 tokens for Claude 3.5 Haiku and Claude 3 Haiku

Shorter prompts cannot be cached, even if marked with cache_control. Any requests to cache fewer than this number of tokens will be processed without caching. To see if a prompt was cached, see the response usage fields.

For concurrent requests, note that a cache entry only becomes available after the first response begins. If you need cache hits for parallel requests, wait for the first response before sending subsequent requests.

The cache has a minimum 5 minute time to live (TTL). Currently, “ephemeral” is the only supported cache type, which corresponds to this minimum 5-minute lifetime.

### ​What can be cached

Every block in the request can be designated for caching with cache_control. This includes:

* Tools: Tool definitions in the tools array
* System messages: Content blocks in the system array
* Messages: Content blocks in the messages.content array, for both user and assistant turns
* Images & Documents: Content blocks in the messages.content array, in user turns
* Tool use and tool results: Content blocks in the messages.content array, in both user and assistant turns

Each of these elements can be marked with cache_control to enable caching for that portion of the request.

### ​Tracking cache performance

Monitor cache performance using these API response fields, within usage in the response (or message_start event if streaming):

* cache_creation_input_tokens: Number of tokens written to the cache when creating a new entry.
* cache_read_input_tokens: Number of tokens retrieved from the cache for this request.
* input_tokens: Number of input tokens which were not read from or used to create a cache.

### ​Best practices for effective caching

To optimize prompt caching performance:

* Cache stable, reusable content like system instructions, background information, large contexts, or frequent tool definitions.
* Place cached content at the prompt’s beginning for best performance.
* Use cache breakpoints strategically to separate different cacheable prefix sections.
* Regularly analyze cache hit rates and adjust your strategy as needed.

### ​Optimizing for different use cases

Tailor your prompt caching strategy to your scenario:

* Conversational agents: Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents.
* Coding assistants: Improve autocomplete and codebase Q&A by keeping relevant sections or a summarized version of the codebase in the prompt.
* Large document processing: Incorporate complete long-form material including images in your prompt without increasing response latency.
* Detailed instruction sets: Share extensive lists of instructions, procedures, and examples to fine-tune Claude’s responses.  Developers often include an example or two in the prompt, but with prompt caching you can get even better performance by including 20+ diverse examples of high quality answers.
* Agentic tool use: Enhance performance for scenarios involving multiple tool calls and iterative code changes, where each step typically requires a new API call.
* Talk to books, papers, documentation, podcast transcripts, and other longform content:  Bring any knowledge base alive by embedding the entire document(s) into the prompt, and letting users ask it questions.

### ​Troubleshooting common issues

If experiencing unexpected behavior:

* Ensure cached sections are identical and marked with cache_control in the same locations across calls
* Check that calls are made within the 5-minute cache lifetime
* Verify that tool_choice and image usage remain consistent between calls
* Validate that you are caching at least the minimum number of tokens
* While the system will attempt to use previously cached content at positions prior to a cache breakpoint, you may use an additional cache_control parameter to guarantee cache lookup on previous portions of the prompt, which may be useful for queries with very long lists of content blocks

Note that changes to tool_choice or the presence/absence of images anywhere in the prompt will invalidate the cache, requiring a new cache entry to be created.

## ​Cache storage and sharing

* Organization Isolation: Caches are isolated between organizations. Different organizations never share caches, even if they use identical prompts..
* Exact Matching: Cache hits require 100% identical prompt segments, including all text and images up to and including the block marked with cache control. The same block must be marked with cache_control during cache reads and creation.
* Output Token Generation: Prompt caching has no effect on output token generation. The response you receive will be identical to what you would get if prompt caching was not used.

## ​Prompt caching examples

To help you get started with prompt caching, we’ve prepared a prompt caching cookbook with detailed examples and best practices.

Below, we’ve included several code snippets that showcase various prompt caching patterns. These examples demonstrate how to implement caching in different scenarios, helping you understand the practical applications of this feature:

Large context caching example

This example demonstrates basic prompt caching usage, caching the full text of the legal agreement as a prefix while keeping the user instruction uncached.

For the first request:

* input_tokens: Number of tokens in the user message only
* cache_creation_input_tokens: Number of tokens in the entire system message, including the legal document
* cache_read_input_tokens: 0 (no cache hit on first request)

For subsequent requests within the cache lifetime:

* input_tokens: Number of tokens in the user message only
* cache_creation_input_tokens: 0 (no new cache creation)
* cache_read_input_tokens: Number of tokens in the entire cached system message

Caching tool definitions

In this example, we demonstrate caching tool definitions.

The cache_control parameter is placed on the final tool (get_time) to designate all of the tools as part of the static prefix.

This means that all tool definitions, including get_weather and any other tools defined before get_time, will be cached as a single prefix.

This approach is useful when you have a consistent set of tools that you want to reuse across multiple requests without re-processing them each time.

For the first request:

* input_tokens: Number of tokens in the user message
* cache_creation_input_tokens: Number of tokens in all tool definitions and system prompt
* cache_read_input_tokens: 0 (no cache hit on first request)

For subsequent requests within the cache lifetime:

* input_tokens: Number of tokens in the user message
* cache_creation_input_tokens: 0 (no new cache creation)
* cache_read_input_tokens: Number of tokens in all cached tool definitions and system prompt

Continuing a multi-turn conversation

In this example, we demonstrate how to use prompt caching in a multi-turn conversation.

The cache_control parameter is placed on the system message to designate it as part of the static prefix.

During each turn, we mark the final message with cache_control so the conversation can be incrementally cached. The system will automatically lookup and use the longest previously cached prefix for follow-up messages.

This approach is useful for maintaining context in ongoing conversations without repeatedly processing the same information.

For each request:

* input_tokens: Number of tokens in the new user message (will be minimal)
* cache_creation_input_tokens: Number of tokens in the new assistant and user turns
* cache_read_input_tokens: Number of tokens in the conversation up to the previous turn

## ​FAQ

What is the cache lifetime?

The cache has a minimum lifetime (TTL) of 5 minutes. This lifetime is refreshed each time the cached content is used.

How many cache breakpoints can I use?

You can define up to 4 cache breakpoints (using cache_control parameters) in your prompt.

Is prompt caching available for all models?

No, prompt caching is currently only available for Claude 3.7 Sonnet, Claude 3.5 Sonnet, Claude 3.5 Haiku, Claude 3 Haiku, and Claude 3 Opus.

How does prompt caching work with extended thinking?

Cached system prompts and tools will be reused when thinking parameters change. However, thinking changes (enabling/disabling or budget changes) will invalidate previously cached prompt prefixes with messages content.

For more detailed information about extended thinking, including its interaction with tool use and prompt caching, see the extended thinking documentation.

How do I enable prompt caching?

To enable prompt caching, include at least one cache_control breakpoint in your API request.

Can I use prompt caching with other API features?

Yes, prompt caching can be used alongside other API features like tool use and vision capabilities. However, changing whether there are images in a prompt or modifying tool use settings will break the cache.

How does prompt caching affect pricing?

Prompt caching introduces a new pricing structure where cache writes cost 25% more than base input tokens, while cache hits cost only 10% of the base input token price.

Can I manually clear the cache?

Currently, there’s no way to manually clear the cache. Cached prefixes automatically expire after a minimum of 5 minutes of inactivity.

How can I track the effectiveness of my caching strategy?

You can monitor cache performance using the cache_creation_input_tokens and cache_read_input_tokens fields in the API response.

What can break the cache?

Changes that can break the cache include modifying any content, changing whether there are any images (anywhere in the prompt), and altering tool_choice.type. Any of these changes will require creating a new cache entry.

How does prompt caching handle privacy and data separation?

Prompt caching is designed with strong privacy and data separation measures:

1. Cache keys are generated using a cryptographic hash of the prompts up to the cache control point. This means only requests with identical prompts can access a specific cache.
2. Caches are organization-specific. Users within the same organization can access the same cache if they use identical prompts, but caches are not shared across different organizations, even for identical prompts.
3. The caching mechanism is designed to maintain the integrity and privacy of each unique conversation or context.
4. It’s safe to use cache_control anywhere in your prompts. For cost efficiency, it’s better to exclude highly variable parts (e.g., user’s arbitrary input) from caching.

These measures ensure that prompt caching maintains data privacy and security while offering performance benefits.

Can I use prompt caching with the Batches API?

Yes, it is possible to use prompt caching with your Batches API requests. However, because asynchronous batch requests can be processed concurrently and in any order, cache hits are provided on a best-effort basis.

Why am I seeing the error `AttributeError: 'Beta' object has no attribute 'prompt_caching'` in Python?

This error typically appears when you have upgraded your SDK or you are using outdated code examples. Prompt caching is now generally available, so you no longer need the beta prefix. Instead of:

Simply use:

Why am I seeing 'TypeError: Cannot read properties of undefined (reading 'messages')'?

This error typically appears when you have upgraded your SDK or you are using outdated code examples. Prompt caching is now generally available, so you no longer need the beta prefix. Instead of:
TypeScript
```
client.beta.promptCaching.messages.create(...)
```

Simply use:

```
client.messages.create(...)
```

Was this page helpful?
YesNo[Token-efficient tool use (beta)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/token-efficient-tool-use)[PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How prompt caching works
* Pricing
* How to implement prompt caching
* Supported models
* Structuring your prompt
* Cache limitations
* What can be cached
* Tracking cache performance
* Best practices for effective caching
* Optimizing for different use cases
* Troubleshooting common issues
* Cache storage and sharing
* Prompt caching examples
* FAQ


---

## Text generation

Source: https://docs.anthropic.com/en/docs/build-with-claude/text-generation

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationText generation[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy

# Text generation

Claude excels in a wide range of text-based tasks. Claude has been trained to ingest code, prose, and other natural language inputs, and provide text outputs in response.

Prompts are best written as natural language queries as if you are instructing someone to do something, with the more detail the better. You can further improve your baseline prompt with prompt engineering.

## ​Text capabilities and use cases

Claude has a broad range of text-based capabilities, including but not limited to:
CapabilityThis enables you to…Text SummarizationDistill lengthy content into key insights for executives, social media, or product teams.Content GenerationCraft compelling content from blog posts and emails to marketing slogans and product descriptions.Data / Entity ExtractionUncover structured insights from unstructured text like reviews, news articles, or transcripts.Question AnsweringBuild intelligent, interactive systems from customer support chatbots to educational AI tutors.Text TranslationSeamlessly communicate across languages in products, support, and content creation.Text Analysis & RecommendationsUnderstand sentiment, preferences, and patterns to personalize user experiences and offerings.Dialogue and ConversationCreate engaging, context-aware interactions in games, virtual assistants, and storytelling apps.Code Explanation & GenerationAccelerate development with instant code reviews, boilerplate generation, and interactive tutorials.
## ​Anthropic Cookbook

Dive into practical examples and hands-on tutorials with our collection of Jupyter notebooks.
[PDF Upload & SummarizationLearn how to upload PDFs and have Claude summarize their content, making it easy to digest long documents.](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/pdf_upload_summarization.ipynb)[Tool Use & Function CallingDiscover how to extend Claude’s capabilities by integrating external tools and functions into your workflows.](https://github.com/anthropics/anthropic-cookbook/tree/main/tool_use)[Embeddings with VoyageAIExplore how to create and use embeddings with VoyageAI for advanced text similarity and search tasks.](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md)
## ​More Resources

From crafting the perfect prompt to understanding API details, we’ve got you covered.
[Prompt Engineering GuideMaster the art of prompt crafting to get the most out of Claude. Especially useful for fine-tuning with legacy models.](https://docs.anthropic.com/en/docs/prompt-engineering)[Prompt LibraryFind a wide range of pre-crafted prompts for various tasks and industries. Perfect for inspiration or quick starts.](https://docs.anthropic.com/en/prompt-library)[API DocumentationEverything you need to interact with Claude via our API: request formats, response handling, and troubleshooting.](https://docs.anthropic.com/en/api/getting-started)
Was this page helpful?
YesNo[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Text capabilities and use cases
* Anthropic Cookbook
* More Resources


---

## Token counting

Source: https://docs.anthropic.com/en/docs/build-with-claude/token-counting

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeToken counting[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Token counting

Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. With token counting, you can

* Proactively manage rate limits and costs
* Make smart model routing decisions
* Optimize prompts to be a specific length

## ​How to count message tokens

The token counting endpoint accepts the same structured list of inputs for creating a message, including support for system prompts, tools, images, and PDFs. The response contains the total number of input tokens.

The token count should be considered an estimate. In some cases, the actual number of input tokens used when creating a message may differ by a small amount.

### ​Supported models

The token counting endpoint supports the following models:

* Claude 3.7 Sonnet
* Claude 3.5 Sonnet
* Claude 3.5 Haiku
* Claude 3 Haiku
* Claude 3 Opus

### ​Count tokens in basic messages
JSON
```
{ "input_tokens": 14 }
```

### ​Count tokens in messages with tools
JSON
```
{ "input_tokens": 403 }
```

### ​Count tokens in messages with images
JSON
```
{ "input_tokens": 1551 }
```

### ​Count tokens in messages with extended thinking

See here for more details about how the context window is calculated with extended thinking

* Thinking blocks from previous assistant turns are ignored and do not count toward your input tokens
* Current assistant turn thinking does count toward your input tokens
JSON
```
{ "input_tokens": 88 }
```

### ​Count tokens in messages with PDFs

Token counting supports PDFs with the same limitations as the Messages API.
JSON
```
{ "input_tokens": 2188 }
```

## ​Pricing and rate limits

Token counting is free to use but subject to requests per minute rate limits based on your usage tier. If you need higher limits, contact sales through the Anthropic Console.
Usage tierRequests per minute (RPM)110022,00034,00048,000
Token counting and message creation have separate and independent rate limits — usage of one does not count against the limits of the other.

## ​FAQ

Does token counting use prompt caching?

No, token counting provides an estimate without using caching logic. While you may provide cache_control blocks in your token counting request, prompt caching only occurs during actual message creation.

Was this page helpful?
YesNo[Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)[Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How to count message tokens
* Supported models
* Count tokens in basic messages
* Count tokens in messages with tools
* Count tokens in messages with images
* Count tokens in messages with extended thinking
* Count tokens in messages with PDFs
* Pricing and rate limits
* FAQ


---

## Using the Evaluation Tool

Source: https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationTest and evaluateUsing the Evaluation Tool[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Test and evaluate
# Using the Evaluation Tool

The Anthropic Console features an Evaluation tool that allows you to test your prompts under various scenarios.

## ​Accessing the Evaluate Feature

To get started with the Evaluation tool:

1. Open the Anthropic Console and navigate to the prompt editor.
2. After composing your prompt, look for the ‘Evaluate’ tab at the top of the screen.



Ensure your prompt includes at least 1-2 dynamic variables using the double brace syntax: {{variable}}. This is required for creating eval test sets.

## ​Generating Prompts

The Console offers a built-in prompt generator powered by Claude 3.7 Sonnet:
1
Click 'Generate Prompt'

Clicking the ‘Generate Prompt’ helper tool will open a modal that allows you to enter your task information.
2
Describe your task

Describe your desired task (e.g., “Triage inbound customer support requests”) with as much or as little detail as you desire. The more context you include, the more Claude can tailor its generated prompt to your specific needs.
3
Generate your prompt

Clicking the orange ‘Generate Prompt’ button at the bottom will have Claude generate a high quality prompt for you. You can then further improve those prompts using the Evaluation screen in the Console.

This feature makes it easier to create prompts with the appropriate variable syntax for evaluation.



## ​Creating Test Cases

When you access the Evaluation screen, you have several options to create test cases:

1. Click the ’+ Add Row’ button at the bottom left to manually add a case.
2. Use the ‘Generate Test Case’ feature to have Claude automatically generate test cases for you.
3. Import test cases from a CSV file.

To use the ‘Generate Test Case’ feature:
1
Click on 'Generate Test Case'

Claude will generate test cases for you, one row at a time for each time you click the button.
2
Edit generation logic (optional)

You can also edit the test case generation logic by clicking on the arrow dropdown to the right of the ‘Generate Test Case’ button, then on ‘Show generation logic’ at the top of the Variables window that pops up. You may have to click `Generate’ on the top right of this window to populate initial generation logic.

Editing this allows you to customize and fine tune the test cases that Claude generates to greater precision and specificity.

Here’s an example of a populated Evaluation screen with several test cases:



If you update your original prompt text, you can re-run the entire eval suite against the new prompt to see how changes affect performance across all test cases.

## ​Tips for Effective Evaluation

Prompt Structure for Evaluation

To make the most of the Evaluation tool, structure your prompts with clear input and output formats. For example:

```
In this task, you will generate a cute one sentence story that incorporates two elements: a color and a sound.
The color to include in the story is:
<color>
{{COLOR}}
</color>
The sound to include in the story is:
<sound>
{{SOUND}}
</sound>
Here are the steps to generate the story:
1. Think of an object, animal, or scene that is commonly associated with the color provided. For example, if the color is "blue", you might think of the sky, the ocean, or a bluebird.
2. Imagine a simple action, event or scene involving the colored object/animal/scene you identified and the sound provided. For instance, if the color is "blue" and the sound is "whistle", you might imagine a bluebird whistling a tune.
3. Describe the action, event or scene you imagined in a single, concise sentence. Focus on making the sentence cute, evocative and imaginative. For example: "A cheerful bluebird whistled a merry melody as it soared through the azure sky."
Please keep your story to one sentence only. Aim to make that sentence as charming and engaging as possible while naturally incorporating the given color and sound.
Write your completed one sentence story inside <story> tags.
```

This structure makes it easy to vary inputs ({{COLOR}} and {{SOUND}}) and evaluate outputs consistently.

Use the ‘Generate a prompt’ helper tool in the Console to quickly create prompts with the appropriate variable syntax for evaluation.

## ​Understanding and comparing results

The Evaluation tool offers several features to help you refine your prompts:

1. Side-by-side comparison: Compare the outputs of two or more prompts to quickly see the impact of your changes.
2. Quality grading: Grade response quality on a 5-point scale to track improvements in response quality per prompt.
3. Prompt versioning: Create new versions of your prompt and re-run the test suite to quickly iterate and improve results.

By reviewing results across test cases and comparing different prompt versions, you can spot patterns and make informed adjustments to your prompt more efficiently.

Start evaluating your prompts today to build more robust AI applications with Claude!

Was this page helpful?
YesNo[Reducing latency](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-latency)[Admin API](https://docs.anthropic.com/en/docs/administration/administration-api)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Accessing the Evaluate Feature
* Generating Prompts
* Creating Test Cases
* Tips for Effective Evaluation
* Understanding and comparing results


---

## Vision

Source: https://docs.anthropic.com/en/docs/build-with-claude/vision

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationBuild with ClaudeVision[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Build with Claude
# Vision

The Claude 3 family of models comes with new vision capabilities that allow Claude to understand and analyze images, opening up exciting possibilities for multimodal interaction.

This guide describes how to work with images in Claude, including best practices, code examples, and limitations to keep in mind.

## ​How to use vision

Use Claude’s vision capabilities via:

* claude.ai. Upload an image like you would a file, or drag and drop an image directly into the chat window.
* The Console Workbench. If you select a model that accepts images (Claude 3 models only), a button to add images appears at the top right of every User message block.
* API request. See the examples in this guide.

## ​Before you upload

### ​Basics and Limits

You can include multiple images in a single request (up to 20 for claude.ai and 100 for API requests). Claude will analyze all provided images when formulating its response. This can be helpful for comparing or contrasting images.

If you submit an image larger than 8000x8000 px, it will be rejected. If you submit more than 20 images in one API request, this limit is 2000x2000 px.

### ​Evaluate image size

For optimal performance, we recommend resizing images before uploading if they are too large. If your image’s long edge is more than 1568 pixels, or your image is more than ~1,600 tokens, it will first be scaled down, preserving aspect ratio, until it’s within the size limits.

If your input image is too large and needs to be resized, it will increase latency of time-to-first-token, without giving you any additional model performance. Very small images under 200 pixels on any given edge may degrade performance.

To improve time-to-first-token, we recommend
resizing images to no more than 1.15 megapixels (and within 1568 pixels in
both dimensions).

Here is a table of maximum image sizes accepted by our API that will not be resized for common aspect ratios. With the Claude 3.7 Sonnet model, these images use approximately 1,600 tokens and around $4.80/1K images.
Aspect ratioImage size1:11092x1092 px3:4951x1268 px2:3896x1344 px9:16819x1456 px1:2784x1568 px
### ​Calculate image costs

Each image you include in a request to Claude counts towards your token usage. To calculate the approximate cost, multiply the approximate number of image tokens by the per-token price of the model you’re using.

If your image does not need to be resized, you can estimate the number of tokens used through this algorithm: tokens = (width px * height px)/750

Here are examples of approximate tokenization and costs for different image sizes within our API’s size constraints based on Claude 3.7 Sonnet per-token price of $3 per million input tokens:
Image size# of TokensCost / imageCost / 1K images200x200 px(0.04 megapixels)~54~$0.00016~$0.161000x1000 px(1 megapixel)~1334~$0.004~$4.001092x1092 px(1.19 megapixels)~1590~$0.0048~$4.80
### ​Ensuring image quality

When providing images to Claude, keep the following in mind for best results:

* Image format: Use a supported image format: JPEG, PNG, GIF, or WebP.
* Image clarity: Ensure images are clear and not too blurry or pixelated.
* Text: If the image contains important text, make sure it’s legible and not too small. Avoid cropping out key visual context just to enlarge the text.

## ​Prompt examples

Many of the prompting techniques that work well for text-based interactions with Claude can also be applied to image-based prompts.

These examples demonstrate best practice prompt structures involving images.

Just as with document-query placement, Claude works best when images come
before text. Images placed after text or interpolated with text will still
perform well, but if your use case allows it, we recommend an image-then-text
structure.

### ​About the prompt examples

The following examples demonstrate how to use Claude’s vision capabilities using various programming languages and approaches. You can provide images to Claude in two ways:

1. As a base64-encoded image in image content blocks
2. As a URL reference to an image hosted online

The base64 example prompts use these variables:

* Python
* TypeScript
* Shell
Python
```
import base64
import httpx

# For base64-encoded images
image1_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
image1_media_type = "image/jpeg"
image1_data = base64.standard_b64encode(httpx.get(image1_url).content).decode("utf-8")

image2_url = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Iridescent.green.sweat.bee1.jpg"
image2_media_type = "image/jpeg"
image2_data = base64.standard_b64encode(httpx.get(image2_url).content).decode("utf-8")

# For URL-based images, you can use the URLs directly in your requests
```

Below are examples of how to include images in a Messages API request using base64-encoded images and URL references:

### ​Base64-encoded image example

* Python
* TypeScript
* Shell
Python
```
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image."
                }
            ],
        }
    ],
)
print(message)
```

### ​URL-based image example

* Python
* TypeScript
* Shell
Python
```
import anthropic

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg",
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image."
                }
            ],
        }
    ],
)
print(message)
```

See Messages API examples for more example code and parameter details.

Example: One image

It’s best to place images earlier in the prompt than questions about them or instructions for tasks that use them.

Ask Claude to describe one image.
RoleContentUser[Image] Describe this image.
Here is the corresponding API call using the Claude 3.7 Sonnet model.

* Using Base64
* Using URL
Python
```
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image."
                }
            ],
        }
    ],
)
```

Example: Multiple images

In situations where there are multiple images, introduce each image with Image 1: and Image 2: and so on. You don’t need newlines between images or between images and the prompt.

Ask Claude to describe the differences between multiple images.
RoleContentUserImage 1: [Image 1] Image 2: [Image 2] How are these images different?
Here is the corresponding API call using the Claude 3.7 Sonnet model.

* Using Base64
* Using URL
Python
```
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Image 1:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Image 2:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image2_media_type,
                        "data": image2_data,
                    },
                },
                {
                    "type": "text",
                    "text": "How are these images different?"
                }
            ],
        }
    ],
)
```

Example: Multiple images with a system prompt

Ask Claude to describe the differences between multiple images, while giving it a system prompt for how to respond.
ContentSystemRespond only in Spanish.UserImage 1: [Image 1] Image 2: [Image 2] How are these images different?
Here is the corresponding API call using the Claude 3.7 Sonnet model.

* Using Base64
* Using URL
Python
```
message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    system="Respond only in Spanish.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Image 1:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image1_media_type,
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Image 2:"
                },
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image2_media_type,
                        "data": image2_data,
                    },
                },
                {
                    "type": "text",
                    "text": "How are these images different?"
                }
            ],
        }
    ],
)
```

Example: Four images across two conversation turns

Claude’s vision capabilities shine in multimodal conversations that mix images and text. You can have extended back-and-forth exchanges with Claude, adding new images or follow-up questions at any point. This enables powerful workflows for iterative image analysis, comparison, or combining visuals with other knowledge.

Ask Claude to contrast two images, then ask a follow-up question comparing the first images to two new images.
RoleContentUserImage 1: [Image 1] Image 2: [Image 2] How are these images different?Assistant[Claude’s response]UserImage 1: [Image 3] Image 2: [Image 4] Are these images similar to the first two?Assistant[Claude’s response]
When using the API, simply insert new images into the array of Messages in the user role as part of any standard multiturn conversation structure.

## ​Limitations

While Claude’s image understanding capabilities are cutting-edge, there are some limitations to be aware of:

* People identification: Claude cannot be used to identify (i.e., name) people in images and will refuse to do so.
* Accuracy: Claude may hallucinate or make mistakes when interpreting low-quality, rotated, or very small images under 200 pixels.
* Spatial reasoning: Claude’s spatial reasoning abilities are limited. It may struggle with tasks requiring precise localization or layouts, like reading an analog clock face or describing exact positions of chess pieces.
* Counting: Claude can give approximate counts of objects in an image but may not always be precisely accurate, especially with large numbers of small objects.
* AI generated images: Claude does not know if an image is AI-generated and may be incorrect if asked. Do not rely on it to detect fake or synthetic images.
* Inappropriate content: Claude will not process inappropriate or explicit images that violate our Acceptable Use Policy.
* Healthcare applications: While Claude can analyze general medical images, it is not designed to interpret complex diagnostic scans such as CTs or MRIs. Claude’s outputs should not be considered a substitute for professional medical advice or diagnosis.

Always carefully review and verify Claude’s image interpretations, especially for high-stakes use cases. Do not use Claude for tasks requiring perfect precision or sensitive image analysis without human oversight.

## ​FAQ

What image file types does Claude support?

Claude currently supports JPEG, PNG, GIF, and WebP image formats, specifically:

* image/jpeg
* image/png
* image/gif
* image/webp

Can Claude read image URLs?

Yes, Claude can now process images from URLs with our URL image source blocks in the API.
Simply use the “url” source type instead of “base64” in your API requests.
Example:

```
{
  "type": "image",
  "source": {
    "type": "url",
    "url": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
  }
}
```

Is there a limit to the image file size I can upload?

Yes, there are limits:

* API: Maximum 5MB per image
* claude.ai: Maximum 10MB per image

Images larger than these limits will be rejected and return an error when using our API.

How many images can I include in one request?

The image limits are:

* Messages API: Up to 100 images per request
* claude.ai: Up to 20 images per turn

Requests exceeding these limits will be rejected and return an error.

Does Claude read image metadata?

No, Claude does not parse or receive any metadata from images passed to it.

Can I delete images I've uploaded?

No. Image uploads are ephemeral and not stored beyond the duration of the API
request. Uploaded images are automatically deleted after they have been
processed.

Where can I find details on data privacy for image uploads?

Please refer to our privacy policy page for information on how we handle
uploaded images and other data. We do not use uploaded images to train our
models.

What if Claude's image interpretation seems wrong?

If Claude’s image interpretation seems incorrect:

1. Ensure the image is clear, high-quality, and correctly oriented.
2. Try prompt engineering techniques to improve results.
3. If the issue persists, flag the output in claude.ai (thumbs up/down) or contact our support team.

Your feedback helps us improve!

Can Claude generate or edit images?

No, Claude is an image understanding model only. It can interpret and analyze images, but it cannot generate, produce, edit, manipulate, or create images.

## ​Dive deeper into vision

Ready to start building with images using Claude? Here are a few helpful resources:

* Multimodal cookbook: This cookbook has tips on getting started with images and best practice techniques to ensure the highest quality performance with images. See how you can effectively prompt Claude with images to carry out tasks such as interpreting and analyzing charts or extracting content from forms.
* API reference: Visit our documentation for the Messages API, including example API calls involving images.

If you have any other questions, feel free to reach out to our support team. You can also join our developer community to connect with other creators and get help from Anthropic experts.

Was this page helpful?
YesNo[Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)[Overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* How to use vision
* Before you upload
* Basics and Limits
* Evaluate image size
* Calculate image costs
* Ensuring image quality
* Prompt examples
* About the prompt examples
* Base64-encoded image example
* URL-based image example
* Limitations
* FAQ
* Dive deeper into vision


---

## Welcome to Claude

Source: https://docs.anthropic.com/en/docs/welcome

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...NavigationGet startedWelcome to Claude[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)[Developer Console](https://console.anthropic.com/)[Developer Discord](https://www.anthropic.com/discord)[Support](https://support.anthropic.com/)
##### Get started

* Overview
* Initial setup
* Intro to Claude

##### Learn about Claude

* Use cases
* Models & pricing
* Security and compliance

##### Build with Claude

* Define success criteria
* Develop test cases
* Context windows
* Vision
* Prompt engineering
* Extended thinking
* Multilingual support
* Tool use (function calling)
* Prompt caching
* PDF support
* Citations
* Token counting
* Batch processing
* Embeddings

##### Agents and tools

* Claude Code
* Computer use (beta)
* Model Context Protocol (MCP)
* Google Sheets add-on

##### Test and evaluate

* Strengthen guardrails
* Using the Evaluation Tool

##### Administration

* Admin API

##### Resources

* Glossary
* Model deprecations
* System status
* Claude 3 model card
* Claude 3.7 system card
* Anthropic Cookbook
* Anthropic Courses

##### Legal center

* Anthropic Privacy Policy
Get started
# Welcome to Claude

Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.
Introducing[Claude 3.7 Sonnet](https://docs.anthropic.com/en/docs/about-claude/models)- our most intelligent model yet. 3.7 Sonnet is the first hybrid[reasoning](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)model on the market. Learn more in our[blog post](https://www.anthropic.com/news/claude-3-7-sonnet).Looking to chat with Claude? Visit[claude.ai](http://www.claude.ai)!
## ​Get started

If you’re new to Claude, start here to learn the essentials and make your first API call.
[Intro to ClaudeExplore Claude’s capabilities and development flow.](https://docs.anthropic.com/en/docs/intro-to-claude)[QuickstartLearn how to make your first API call in minutes.](https://docs.anthropic.com/en/docs/quickstart)[Prompt LibraryExplore example prompts for inspiration.](https://docs.anthropic.com/en/prompt-library/library)
## ​Develop with Claude

Anthropic has best-in-class developer tools to build scalable applications with Claude.
[Developer ConsoleEnjoy easier, more powerful prompting in your browser with the Workbench and prompt generator tool.](https://console.anthropic.com)[API ReferenceExplore, implement, and scale with the Anthropic API and SDKs.](https://docs.anthropic.com/en/api/getting-started)[Anthropic CookbookLearn with interactive Jupyter notebooks that demonstrate uploading PDFs, embeddings, and more.](https://github.com/anthropics/anthropic-cookbook)
## ​Key capabilities

Claude can assist with many tasks that involve text, code, and images.
[Text and code generationSummarize text, answer questions, extract data, translate text, and explain and generate code.](https://docs.anthropic.com/en/docs/build-with-claude/text-generation)[VisionProcess and analyze visual input and generate text and code from images.](https://docs.anthropic.com/en/docs/build-with-claude/vision)
## ​Support
[Help CenterFind answers to frequently asked account and billing questions.](https://support.anthropic.com/en/)[Service StatusCheck the status of Anthropic services.](https://www.anthropic.com/status)
Was this page helpful?
YesNo[Initial setup](https://docs.anthropic.com/en/docs/initial-setup)[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)On this page
* Get started
* Develop with Claude
* Key capabilities
* Support


---

## extended-thinking

Source: https://docs.anthropic.com/en/docs/en/docs/build-with-claude/extended-thinking

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...Navigation[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)Build with
Learn how to get started with the Anthropic API and Claude.
Help me get started with prompt caching…[Explore the docs](https://docs.anthropic.com/en/docs/welcome)
Get started with tools and guides
[Get startedMake your first API call in minutes.](https://docs.anthropic.com/en/docs/initial-setup)[API ReferenceIntegrate and scale using our API and SDKs.](https://docs.anthropic.com/en/api/getting-started)[Anthropic ConsoleCraft and test powerful prompts directly in your browser.](https://console.anthropic.com)[Anthropic CoursesExplore Anthropic’s educational courses and projects.](https://github.com/anthropics/courses)[Anthropic CookbookSee replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[Anthropic QuickstartsDeployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

## models

Source: https://docs.anthropic.com/en/docs/en/docs/about-claude/models

[Anthropic home page](https://docs.anthropic.com/)EnglishSearch...
* Research
* News
* Go to claude.ai
* Go to claude.ai
Search...Navigation[Welcome](https://docs.anthropic.com/en/home)[User Guides](https://docs.anthropic.com/en/docs/welcome)[API Reference](https://docs.anthropic.com/en/api/getting-started)[Prompt Library](https://docs.anthropic.com/en/prompt-library/library)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)[Developer Newsletter](https://docs.anthropic.com/en/developer-newsletter/overview)Build with
Learn how to get started with the Anthropic API and Claude.
Help me get started with prompt caching…[Explore the docs](https://docs.anthropic.com/en/docs/welcome)
Get started with tools and guides
[Get startedMake your first API call in minutes.](https://docs.anthropic.com/en/docs/initial-setup)[API ReferenceIntegrate and scale using our API and SDKs.](https://docs.anthropic.com/en/api/getting-started)[Anthropic ConsoleCraft and test powerful prompts directly in your browser.](https://console.anthropic.com)[Anthropic CoursesExplore Anthropic’s educational courses and projects.](https://github.com/anthropics/courses)[Anthropic CookbookSee replicable code samples and implementations.](https://github.com/anthropics/anthropic-cookbook)[Anthropic QuickstartsDeployable applications built with our API.](https://github.com/anthropics/anthropic-quickstarts)

---

