from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/schedule', methods=['POST'])
def schedule_interviews():
    try:
        data = request.json
        start_times = data['start_times']
        end_times = data['end_times']
        
        if len(start_times) != len(end_times):
            return jsonify({'error': 'Start times and end times lists must have the same length'}), 400

        # Pairing start and end times and sorting by end time
        interviews = sorted(zip(start_times, end_times), key=lambda x: x[1])

        max_interviews = 0
        current_end_time = 0

        for start, end in interviews:
            if start >= current_end_time:
                max_interviews += 1
                current_end_time = end

        return jsonify({'max_interviews': max_interviews}), 200
    except KeyError:
        return jsonify({'error': 'Invalid JSON format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
