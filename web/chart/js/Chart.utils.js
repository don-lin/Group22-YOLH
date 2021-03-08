class BaseChart {
  constructor(id, data) {
    this.ctx = document.getElementById(id);
    this.chart = new Chart(this.ctx, data);
  }

  update() {
    this.chart.update();
  }

  removeData(label) {
    const lines = this.chart.data.datasets;
    for (let i = 0; i < lines.length; i++) {
      if (lines[i].label === label) lines.splice(i, 1);
    }
  }
}

class Line extends BaseChart {
  constructor(id, xLabels) {
    const data = {
      type: "line",
      data: {
        labels: xLabels,
      },
      options: {},
    };

    super(id, data);
  }

  appendLine(label, data, color) {
    const line = {
      label,
      data,
      fill: false,
      borderColor: color,
      lineTension: 0.1,
    };
    this.chart.data.datasets.push(line);
    this.update();
  }
}
