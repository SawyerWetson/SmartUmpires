<?php
// Path to the CSV file
$csvFile = __DIR__ . '/StoredData.CSV';

// Get data to log (from POST request, for example)
$dataToStore = [
    'timestamp' => date('Y-m-d H:i:s'),
    'user'      => $_POST['user'] ?? 'unknown',
    'action'    => $_POST['action'] ?? 'none',
    'details'   => $_POST['details'] ?? ''
];

// Open the file for appending
$file = fopen($csvFile, 'a');
if ($file === false) {
    http_response_code(500);
    echo "Error: Unable to open file.";
    exit;
}

// If file is new, write the header row
if (filesize($csvFile) === 0) {
    fputcsv($file, array_keys($dataToStore));
}

// Write the data row
fputcsv($file, $dataToStore);

// Close the file
fclose($file);

// Output success
echo "Data stored successfully.";
?>
