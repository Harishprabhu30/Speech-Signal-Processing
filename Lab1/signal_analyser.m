% writing function

function y = signal_analyser(start_time, end_time)
    [audiofile, location] = uigetfile(".wav");
    if isequal(audiofile, 0)
        disp("User Selected Cancel")
    else
        disp(["File Imported: ", fullfile(location, audiofile)])
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

    % getting the time vector of the audiofile
    prompt_1 = "Enter start time for the signal: ";
    prompt_2 = "Enter end time for the signal: ";
    start_time = input(prompt_1); 
    end_time = input(prompt_2);

    start_sample = round(start_time * fs) + 1;
    end_sample = round(end_time * fs);

    t = (0 : num_of_samples - 1) / fs; % in seconds
    y_selected = y(start_sample : end_sample, :);
    t_selected = (start_sample : end_sample) / fs;

    % Converting to milliseconds (ms)
    t_selected_ms = t_selected * 1000;
    t_ms = t * 1000; % time vector in milliseconds

    % Viz
    if info.NumChannels == 2
    
        fprintf("The audio file is Stereo.\n")
        % Extracting Left and Right Channel
        left_channel = y(:, 1);
        right_channel = y(:, 2);
    
        subplot(2, 1, 1);
        plot(t_selected_ms, left_channel(start_sample : end_sample));
        xlabel("Time (milliseconds)");
        ylabel("Amplitude");
        title("Waveform of the Audio File (Left Channel)");
        grid on;

        subplot(2, 1, 2);
        plot(t_selected_ms, right_channel(start_sample : end_sample));
        xlabel("Time (milliseconds)");
        ylabel("Amplitude");
        title("Waveform of the Audio File (Right Channel)");
        grid on;

    else
        fprintf("The audio file is Mono.\n")
        plot(t_selected_ms, y_selected);
        xlabel("Time (milliseconds)")
        ylabel("Amplitude");
        title("Waveform of the Audio File (MONO)")
        grid on;
    end


end
