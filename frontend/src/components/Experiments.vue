<template>
  <div class="Experiments">
    <div class="operator" align="center">
      <span>抽查模型(单选)</span>
      <el-select v-model="model" placeholder="请选择检查模型" @change="getMethods">
        <el-option
          clearable
          v-for="item in modelsTargets"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <span>算法列表(多选)</span>
      <el-select v-model="machineMethods" collapse-tags multiple placeholder="请选择检查模型">
        <el-option
          v-for="item in methodsTargets"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-button type="primary" @click="getData">获取结果</el-button>
    </div>
    <br>
    <br>
    <charts :options="genOption()" align="center"></charts>
    <el-table
    :data="dataArray.ranks"
    stripe
    style="width: 100%">
    <el-table-column
      align="center"
      prop="value"
      label="排名">
    </el-table-column>
    </el-table>
    </div>
</template>
<script>
export default {
  name: 'Experiments',
  data () {
    return {
      dataArray: {
        scores: [],
        names: [],
        ranks: []
      },
      binaryMethods: [
        {
          label: 'LogisticRegression',
          value: 'LogisticRegression'
        },
        {
          label: 'RidgeClassifier',
          value: 'RidgeClassifier'
        },
        {
          label: 'SGDClassifier',
          value: 'SGDClassifier'
        },
        {
          label: 'PassiveAggressiveClassifier',
          value: 'PassiveAggressiveClassifier'
        },
        {
          label: 'KNeighborsClassifier',
          value: 'KNeighborsClassifier'
        },
        {
          label: 'DecisionTreeClassifier',
          value: 'DecisionTreeClassifier'
        },
        {
          label: 'ExtraTreeClassifier',
          value: 'ExtraTreeClassifier'
        },
        {
          label: 'SVC',
          value: 'SVC'
        },
        {
          label: 'GaussianNB',
          value: 'GaussianNB'
        },
        {
          label: 'AdaBoostClassifier',
          value: 'AdaBoostClassifier'
        },
        {
          label: 'BaggingClassifier',
          value: 'BaggingClassifier'
        },
        {
          label: 'RandomForestClassifier',
          value: 'RandomForestClassifier'
        },
        {
          label: 'ExtraTreesClassifier',
          value: 'ExtraTreesClassifier'
        },
        {
          label: 'GradientBoostingClassifier',
          value: 'GradientBoostingClassifier'
        }
      ],
      regressionMethods: [
        {
          label: 'LinearRegression',
          value: 'LinearRegression'
        },
        {
          label: 'Lasso',
          value: 'Lasso'
        },
        {
          label: 'Ridge',
          value: 'Ridge'
        },
        {
          label: 'ElasticNet',
          value: 'ElasticNet'
        },
        {
          label: 'HuberRegressor',
          value: 'HuberRegressor'
        },
        {
          label: 'Lars',
          value: 'Lars'
        },
        {
          label: 'LassoLars',
          value: 'LassoLars'
        },
        {
          label: 'PassiveAggressiveRegressor',
          value: 'PassiveAggressiveRegressor'
        },
        {
          label: 'RANSACRegressor',
          value: 'RANSACRegressor'
        },
        {
          label: 'SGDRegressor',
          value: 'SGDRegressor'
        },
        {
          label: 'TheilSenRegressor',
          value: 'TheilSenRegressor'
        },
        {
          label: 'KNeighborsRegressor',
          value: 'KNeighborsRegressor'
        },
        {
          label: 'DecisionTreeRegressor',
          value: 'DecisionTreeRegressor'
        },
        {
          label: 'ExtraTreeRegressor',
          value: 'ExtraTreeRegressor'
        },
        {
          label: 'SVR',
          value: 'SVR'
        },
        {
          label: 'AdaBoostRegressor',
          value: 'AdaBoostRegressor'
        },
        {
          label: 'BaggingRegressor',
          value: 'BaggingRegressor'
        },
        {
          label: 'RandomForestRegressor',
          value: 'RandomForestRegressor'
        },
        {
          label: 'ExtraTreesRegressor',
          value: 'ExtraTreesRegressor'
        },
        {
          label: 'GradientBoostingRegressor',
          value: 'GradientBoostingRegressor'
        }
      ],
      model: '',
      machineMethods: [],
      modelsTargets: [
        {
          label: '二元分类_1',
          value: 'check_1'
        },
        {
          label: '线性回归',
          value: 'check_2'
        },
        {
          label: '二元分类_2(xgb)',
          value: 'check_3'
        },
        {
          label: '二元分类_3',
          value: 'check_4'
        },
        {
          label: '二元分类_4',
          value: 'check_5'
        }
      ],
      methodsTargets: [],
      shown: false
    }
  },
  methods: {
    genOption () {
      let echarts = require('echarts')
      require('echarts/src/chart/graph')
      echarts.dataTool = require('echarts/extension/dataTool')
      let scores = this.dataArray.scores
      let names = this.dataArray.names
      let data = echarts.dataTool.prepareBoxplotData(scores)
      let option = {
        title: [
          {
            text: 'spot-check-machine-learning-algorithms-in-python',
            left: 'center'
          },
          {
            borderColor: '#999',
            borderWidth: 1,
            textStyle: {
              fontSize: 14
            },
            left: '10%',
            top: '90%'
          }
        ],
        tooltip: {
          trigger: 'item',
          axisPointer: {
            type: 'shadow'
          }
        },
        grid: {
          left: '10%',
          right: '10%',
          bottom: '15%'
        },
        xAxis: {
          type: 'category',
          data: names,
          boundaryGap: true,
          axisLabel: {
            margin: 2,
            interval: 0,
            rotate: 40
          }
        },
        yAxis: {
          type: 'value',
          splitArea: {
            show: true
          }
        },
        series: [
          {
            name: 'boxplot',
            type: 'boxplot',
            data: data.boxData
          },
          {
            name: 'outlier',
            type: 'scatter',
            data: data.outliers
          }
        ]
      }
      return option
    },
    getData () {
      console.log(this.machineMethods)
      this.shown = true
      this.$http.get('/api/checks', {
        params: {
          name: this.model,
          methods: JSON.stringify(this.machineMethods)
        }
      }).then(response => {
        let names = response.data.names
        let scores = response.data.scores
        let ranks = response.data.ranks
        this.dataArray.names = JSON.parse(names)
        this.dataArray.scores = JSON.parse(scores)
        this.dataArray.ranks = JSON.parse(ranks)
        console.log(response)
        this.shown = false
      })
    },
    getMethods () {
      console.log(this.model)
      console.log('message')
      this.machineMethods = []
      this.methodsTargets = []
      if (this.model === 'check_2') {
        this.methodsTargets = this.regressionMethods
      } else {
        this.methodsTargets = this.binaryMethods
      }
      console.log(this.methodsTargets)
    }
  }
}
</script>

<style scoped>
  .echarts {
    width: 100%;
  }
  .el-dialog {
    position: absolute;
    top: 50%;
    left: 50%;
    margin: 0 !important;
    transform: translate(-50%, -50%);
    max-height: calc(100% - 30px);
    max-width: calc(100% - 30px);
    display: flex;
    flex-direction: column;
  }
</style>
