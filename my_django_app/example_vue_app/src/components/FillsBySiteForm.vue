<template>
  <div class="component-container">
    <div class="form-container">
      <div class="form-group">
        <label>Site:</label>
        <select id="form-site-choice" v-model="selectedSitePk">
          <option disabled value="">Select a site</option>
          <option v-for="(site, index) in siteDropdownChoices" :key="index" :value="site.pk">
            {{site.name}}
          </option>
        </select>
        <div v-if="fieldErrors.site" class="form-field-errors">
          <div v-for="(error, index) in fieldErrors.site" :key="index">{{ error }}</div>
        </div>
      </div>
      <div class="form-group">
        <label>Show fills for:</label>
        <select v-model="formMode">
          <option value="count">5000 logs</option>
          <option value="date_range">Date range</option>
        </select>
      </div>
      <template v-if="formMode === 'count'">
        <label>Skip this many recent logs:</label>
        <input v-model.number="countStart">
      </template>
      <template v-else>
        <div class="form-group">
          <label for="form-start-date">Start date:</label>
          <input type="date" id="form-start-date" v-model.lazy="startDateString">
        </div>
        <div class="form-group">
          <label for="form-end-date">End date:</label>
          <input type="date" id="form-end-date" v-model.lazy="endDateString">
        </div>
      </template>
      <div class="form-group">
        <label>Report format:</label>
        <select v-model="reportFormat">
          <option value="csv">Comma-separated (CSV)</option>
          <option value="xlsx">Microsoft Excel (xlsx)</option>
        </select>
      </div>
      <div class="form-group">
        <a v-if="enableSubmitButton" class="btn" :href="submitUrl">Get Report</a>
        <a v-else class="btn">Get Report</a>
      </div>
    </div>
    <div v-if="formErrors.length > 0" class="form-error-container">
      <div v-for="(error, index) in formErrors" :key="index">{{error}}</div>
    </div>
    <div class="btn-container">
      <div v-if="tooManyDays || tooFewDays" class="btn" @click="fixStartDate">Set start date {{maximumDays}} days before end</div>
      <div v-if="tooManyDays || tooFewDays" class="btn" @click="fixEndDate">Set end date {{maximumDays}} days after start</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FillsBySiteForm",
  props: {
    siteList: {
      type: Array,
      default() {return [
        {
          'pk': 'b1907558-274a-4049-b021-d4d34c48f517',
          'name': 'Default site'
        }
      ]}
    }
  },
  data() {
    const maxDays = 30
    let today = new Date()
    let startDate = this.addDays(today, -maxDays)
    return {
      formMode: 'count',
      countStart: 0,
      startDateString: startDate.toISOString().substr(0, 10),
      endDateString: today.toISOString().substr(0,10),
      maximumDays: maxDays,
      minimumDays: 0,
      selectedSitePk: '',
      reportFormat: 'xlsx',
    }
  },
  computed: {
    siteDropdownChoices() {
      let choices = []
      for (let site of this.siteList) {
        choices.push({
          'pk': site.pk,
          'name': site.name
        })
      }
      return choices
    },
    startDate() {
      return new Date(this.startDateString)
    },
    endDate() {
      return new Date(this.endDateString)
    },
    daysDifference() {
      // convert difference in milliseconds to difference in days
      return Math.floor((this.endDate - this.startDate) / (1000 * 60 * 60 * 24))
    },
    tooFewDays() {
      return this.daysDifference < this.minimumDays
    },
    tooManyDays() {
      return this.daysDifference > this.maximumDays
    },
    formErrors() {
      let errors = [];
      if (this.tooFewDays) {
        errors.push("The start date must be on or before the end date")
      }
      if (this.tooManyDays) {
        errors.push(`The start and end date must be no more than 30 days apart. You have selected dates ${this.daysDifference} days apart.`)
      }
      return errors
    },
    submitUrl() {
      if (this.formErrors.length > 0 || this.selectedSitePk === '') {
        return '#'
      }
      if (this.formMode === 'count') {
        return `/v1/qar_fills/site/${this.selectedSitePk}/${this.formMode}/${this.countStart}/5000/?report_format=${this.reportFormat}`
      }
      return `/v1/qar_fills/site/${this.selectedSitePk}/${this.formMode}/${this.startDateString}/${this.endDateString}/?report_format=${this.reportFormat}`
    },
    enableSubmitButton() {
      return this.submitUrl !== '#'
    },
    fieldErrors() {
      let allFieldErrors = {}
      let siteErrors =this.validateSite(this.selectedSitePk)
      if (siteErrors.length > 0) {
        allFieldErrors['site'] = siteErrors
      }
      return allFieldErrors
    }
  },
  methods: {
    addDays(date, days){
      let result = new Date(date);
      result.setDate(result.getDate() + days);
      return result;
    },
    fixStartDate() {
      let newStartDate = this.addDays(this.endDate, -this.maximumDays)
      this.startDateString = `${newStartDate.toISOString().substr(0,10)}`
    },
    fixEndDate() {
      let newEndDate = this.addDays(this.startDate, this.maximumDays)
      this.endDateString = `${newEndDate.toISOString().substr(0,10)}`
    },
    validateSite(value) {
      let errors = [];
      if (value === '') {
        errors.push('Please select a site')
      }
      return errors
    }
  }
}
</script>

<style scoped>
.component-container {
  font-family: sans-serif;
  display: flex;
  flex-flow: column nowrap;
  flex: 1;
  justify-content: flex-start;
  align-items: center;
}
.form-container {
  display: flex;
  flex-flow: row wrap;
  justify-content: center;
  align-items: flex-start;
}
.form-group {
  margin: 0 5px;
}
.form-group > * {
  margin: 0 3px;
}
.form-error-container {
  margin-top: 30px;
  text-align: left;
  color: red;
}
.form-field-errors {
  color: red;
  font-size: small;
  text-align: left;
}
.btn {
  border: 2px solid black;
  border-radius: 10px;
  padding: 0.5rem;
  margin: 0.5rem;
}
a.btn {
  border-color: dimgrey;
  background-color: lightgrey;
  color: dimgrey;
  text-decoration: none;
  cursor: not-allowed;
}
a.btn[href] {
  border-color: forestgreen;
  background: none;
  color: forestgreen;
  cursor: pointer;
}
.btn-container {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  justify-content: center;
}
</style>