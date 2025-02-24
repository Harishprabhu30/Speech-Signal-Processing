% uigetfile: Opens a file with specified extension

% [file, location] = uigetfile(".wav");
% if isequal(file, 0)
%     disp("User Selected Cancel");
% else
%     disp(["User Selected: ", fullfile(location, file)]);
% 
% end


% uiputfile: Saves a File
% 
% [file, location] = uiputfile("lab1.m");
% if isequal(file, 0)
%     disp("saving Failed...")
% else
%     disp("Save Successfull...")
% 
% end

%% Program LAB 1

close all;

[audiofile, loaction] = uigetfile("oh no.wav");
if isequal(audiofile, 0)
    disp("User Selected Cancel")
else
    disp(["File Imported: ", fullfile(loaction, audiofile)])
end

% Reading the audiofile
[y, fs] = audioread(audiofile);


% Play the sound
sound(y, fs);

% Getting the info of the audiofile
info = audioinfo(audiofile);
quantization_bit = info.BitsPerSample;

num_of_samples = length(y); % duration * fs (sampling rate)
fprintf('The sample rate of the audiofile: %d\n', fs);
fprintf('Number of Samples in the audiofile: %d\n', num_of_samples);
fprintf('The Channel of the audiofile: %d\n', size(y, 2));
% fprintf('The length of the audiofile: %d\n', length(y)); % length and size(y,1) are same.

% Calculating the duration of the sample:
% duration = num_of_samples / fs;
fprintf('The duration of the audiofile: %d seconds.\n', info.Duration);
fprintf('Quantization bit of the audiofile: %d bit\n', quantization_bit);

time_step = 1 / fs;
% fprintf('The time step of the audiofile: %d\n', time_step);

% getting the time vector of the audiofile
start_time = 1;
end_time = 2;
start_sample = round(start_time * fs) + 1;
end_sample = round(end_time * fs);

t = (0 : num_of_samples - 1) / fs; % in seconds
y_selected = y(start_sample : end_sample, :);
t_selected = (start_sample : end_sample) / fs;
t_selected_ms = t_selected * 1000;
t_ms = t * 1000; % time vector in milliseconds

% Viz

if info.NumChannels == 2
    
    fprintf("The audio file is Stereo.\n")
    % Extracting Left and Right Channel
    left_channel = y(:, 1);
    right_channel = y(:, 2);
    
    subplot(2, 1, 1);
    plot(t_ms, left_channel);
    xlabel("Time (milliseconds)");
    ylabel("Amplitude");
    title("Waveform of the Audio File (Left Channel)");
    grid on;

    subplot(2, 1, 2);
    plot(t_ms, right_channel);
    xlabel("Time (milliseconds)");
    ylabel("Amplitude");
    title("Waveform of the Audio File (Right Channel)");
    grid on;

else
    fprintf("The audio file is Mono.\n")
    plot(t_ms, y);
    xlabel("Time (milliseconds)")
    ylabel("Amplitude");
    title("Waveform of the Audio File (MONO)")
    grid on;
end