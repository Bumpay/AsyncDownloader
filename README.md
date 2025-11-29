# AsyncDownloader
An asynchronous web-downloader that achieves a overall faster download time of multiple URLs than downloading everything sequential.

## Functional Criteria

### 1. Objective

The system provides an application capable of downloading multiple web resources (e.g., HTML pages, files, APIs) simultaneously. The aim is to significantly reduce overall download time compared to purely sequential downloads.
Users can specify URLs, and the application downloads all resources, shows progress, and saves the results locally.

### 2. Application Scope

This tool is intended for developers or tech-savvy users who want to fetch and save many URLs at once.
Typical use cases:
- Downloading a list of web pages
- Bulk downloading API results
- Testing server responses to parallel requests

### 3. Product Features
#### 3.1 URL Input
- Accepts lists of URLs.
- URLs can be read from a text or CSV file, or passed as CLI parameters.
- Invalid URLs are detected and reported.

#### 3.2 Parallel Downloading
- Downloads are performed concurrently.
- Users can configure the maximum number of parallel downloads.
- When the limit is reached, extra downloads are queued automatically.

#### 3.3 Storage & Filenames
- Downloaded content is saved locally.
- Target directory is configurable.
- Automatically generates filenames if none given (e.g. based on URL, timestamp, or hash).
- Files are not overwritten; unique names are generated in case of collisions.

#### 3.4 Progress & Status Display
- Progress shown, including at least:
    - Total number of downloads
    - Number of completed downloads
    - Number of failed downloads
    - Optional: Estimated remaining time

#### 3.5 Error Handling
- Robust recognition and logging of errors per URL, such as:
    - Timeout
    - HTTP error codes
    - Connection errors
    - Invalid URL
- Failed downloads do not block others.
- Configurable retry attempts for failed downloads.

#### 3.6 Logging
- Logs must store at least:
    - Start & end of process
    - Successful and failed downloads with URL
    - Error causes
- Log output can be written to a file.

### 4. Quality Requirements
#### 4.1 Performance
- Must handle large numbers of URLs (at least 1,000) without hanging or being extremely slow.
- Total time should be significantly reduced via parallelization compared to sequential download.

#### 4.2 Reliability
- Errors on single URLs must not terminate overall process.
- Aborting or closing app should safely end or finish downloads.

#### 4.3 Usability
- Simple command line use.
- Parameters for:
    - Target directory
    - Max parallel downloads
    - Timeout
    - Retry count

#### 4.4 Maintainability
- Well-structured, well-documented code.
- Configurations should be adjustable outside of code (e.g. YAML/JSON or CLI flags).

### 5. Constraints
#### 5.1 Technical Constraints
- Must be implemented in Python.
- Only use platform-independent libraries (Windows, Linux, macOS).
- Internet access required.

#### 5.2 Security Requirements
- Existing files must not be overwritten.
- Do not save unencrypted passwords or sensitive data.
- HTTPS connections must be supported.

#### 5.3 License / Usage
- May be used by third parties without licensing issues (no proprietary dependencies).

### 6. Acceptance Criteria
- A list of at least 1000 URLs can be processed successfully.
- Configurable parallelism works and is limited as expected.
- Successful downloads are saved in the target directory.
- Failed downloads are logged.
- Progress is visible during execution.
- The application runs stably and does not crash on errors.
